import React from "react";
import { Box, Flex } from "@chakra-ui/react";
import { Link } from "react-router-dom";
import MessageCard from "chains/MessageCard";

export const MessageCardList = ({ messages = [] }) => {
  

  return (
    <Flex align="center" justify="left" flexWrap="wrap">
      {messages.map((message) => (
        <Box key={chain.id} p={5} width="400px">
          <Link >
            <MessageCard message={message} />
          </Link>
        </Box>
      ))}
    </Flex>
  );
};
