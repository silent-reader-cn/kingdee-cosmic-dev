# 历史对话附加详情-mai_chathistory_attach

## 历史对话附加详情-主表 t_mai_chathistory_attach

- **表名称：** 历史对话附加详情-主表
- **表名：** t_mai_chathistory_attach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdetail | 详情 | varchar | 255 |  | √ | ' ' | 详情 |
| 3 | fprocessid | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 4 | fdetail_tag | 详情_详情 | text | 0 |  |  | null | 详情_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_chathistory_attach |  | fid |
| 2 | idx_mai_attach_fprocessid |  | fprocessid |
