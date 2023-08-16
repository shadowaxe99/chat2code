const ChainGraphEditor = ({ graph }) => {
  const reactFlowWrapper = useRef(null);
  const edgeUpdate = useRef(true);
  const [chainRef, setChainRef] = useState(graph?.chain);
  const [chainLoaded, setChainLoaded] = useState(graph?.chain !== undefined);
  const { call: loadChain } = useAxios();

  const reactFlowGraph = useGraphForReactFlow(graph);
  const [nodes, setNodes, onNodesChange] = useNodesState(reactFlowGraph.nodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(reactFlowGraph.edges);
  const [reactFlowInstance, setReactFlowInstance] = useState(null);
  const { colorMode } = useColorMode();
  const toast = useToast();
  const navigate = useNavigate();

  const onAPIError = useCallback((err) => {
    toast({
      title: "Error",
      description: `Failed to save chain. ${err.message}`,
      status: "error",
      duration: 10000,
      isClosable: true,
    });
  }, []);

  const api = useChainEditorAPI({
    chain: chainRef,
    onError: onAPIError,
    reactFlowInstance,
  });

  // handle dragging a node onto the graph
  const onDragOver = useCallback((event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = "move";
  }, []);

  const onNodeSaved = useCallback(
    (response) => {
      // first node creates the new chain
      // redirect to the correct URL
      if (!chainLoaded) {
        navigate(`/chains/${response.data.chain_id}`, { replace: true });
        loadChain(`/api/chains/${response.data.chain_id}`, {
          onSuccess: (response) => {
            setChainRef(response.data);
            setChainLoaded(true);
          },
          onError: onAPIError
        });
      }
    },
    [chainRef?.id, chainLoaded]
  );

  const onDrop = useCallback(
    (event) => {
      event.preventDefault();
      const reactFlowBounds = reactFlowWrapper.current.getBoundingClientRect();
      const type = event.dataTransfer.getData('application/reactflow');
      const position = reactFlowInstance.project({
        x: event.clientX - reactFlowBounds.left,
        y: event.clientY - reactFlowBounds.top,
      });
      const newNode = {
        id: uuidv4(),
        type,
        position,
        data: { label: `${type} node` },
      };

      setNodes((ns) => ns.concat(newNode));

      api.createNode(newNode, {
        onSuccess: onNodeSaved,
        onError: onAPIError
      });
    },
    [reactFlowInstance, reactFlowWrapper, setNodes, api, onNodeSaved]
  );

  const onEdgeUpdateStart = useCallback(
    (event, edge) => {
      // reset flag when edge is grabbed
      edgeUpdate.edge = edge;
      edgeUpdate.toHandle = false;
    },
    [setEdges]
  );

  const onEdgeUpdate = useCallback(
    (oldEdge, newConnection) => {
      // update edge if dropped on valid handle
      edgeUpdate.toHandle = true;
      setEdges((els) => updateEdge(oldEdge, newConnection, els));
      if (newConnection.source === "root") {
        if (oldEdge.target !== newConnection.target) {
          api.setRoot({ chain_id: chainRef.id, node_id: newConnection.target });
        }
      } else {
        const isSame =
          oldEdge.source === newConnection.source &&
          oldEdge.target === newConnection.target;
        if (!isSame) {
          api.updateEdge(oldEdge.data.id, {
            source_id: newConnection.source,
            target_id: newConnection.target,
          });
        }
      }
    },
    [chainRef?.id, setEdges]
  );

  const onEdgeUpdateEnd = useCallback(
    (_, edge) => {
      // delete edge if dropped on graph
      if (!edgeUpdate.toHandle) {
        setEdges((eds) => eds.filter((e) => e.id !== edge.id));
        if (edge.source === "root") {
          api.setRoot(chainRef.id, { node_id: null });
        } else {
          api.deleteEdge(edge.data.id);
        }
      }
      edgeUpdate.edge = null;
    },
    [chainRef?.id, setEdges]
  );

  const { callback: debouncedChainUpdate } = useDebounce((...args) => {
    api.updateChain(...args);
  }, 1000);

  const { callback: debouncedChainCreate } = useDebounce((...args) => {
    api.createChain(...args);
  }, 1000);

  return {
    reactFlowWrapper,
    nodes,
    edges,
    onDragOver,
    onDrop,
    onEdgeUpdate,
    onEdgeUpdateStart,
    onEdgeUpdateEnd,
    onLoad: setReactFlowInstance,
    onNodesChange,
    onEdgesChange,
    debouncedChainUpdate,
    debouncedChainCreate,
    chainLoaded,
    chainRef,
    createChainLoading,
    updateChainLoading,
    setRootLoading,
  };
};

export default ChainGraphEditor;