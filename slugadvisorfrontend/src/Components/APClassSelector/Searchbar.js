import React from 'react';
import Select from 'react-select';

const SearchBar = ({ items, onChange }) => {
  const options = items.map((item) => ({ value: item, label: item }));

  return (
    <Select
      options={options}
      isMulti
      placeholder="Select classes..."
      onChange={(selectedOptions) => {
        const selectedItems = selectedOptions.map((option) => option.value);
        onChange(selectedItems);
      }}
      isSearchable
    />
  );
};

export default SearchBar;
