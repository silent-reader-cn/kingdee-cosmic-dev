# 可视化业务流程节点-xkbus_flow_node

## 可视化业务流程节点-多语言表 t_xk_bus_flow_node_l

- **表名称：** 可视化业务流程节点-多语言表
- **表名：** t_xk_bus_flow_node_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_bus_flow_node_l |  | fpkid |
| 2 | idx_t_bf_node_l_fid |  | fid |

---

## 可视化业务流程节点-主表 t_xk_bus_flow_node

- **表名称：** 可视化业务流程节点-主表
- **表名：** t_xk_bus_flow_node

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 3 | fbusflowid | 业务流程 | int8 | 64 |  | √ | 0 | [可视化业务流程 xkbus_flow](../xkbase_files/xkbus_flow.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_bus_flow_node |  | fid |
| 2 | idx_t_bf_node_flowid |  | fbusflowid |
