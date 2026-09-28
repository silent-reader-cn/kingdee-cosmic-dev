# 可视化业务流程初始节点-xkbf_init_node

## 可视化业务流程初始节点-主表 t_xk_bf_init_node

- **表名称：** 可视化业务流程初始节点-主表
- **表名：** t_xk_bf_init_node

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 所属分组 | int8 | 64 |  | √ | 0 | [可视化业务流程初始节点分组 xkbf_init_node_gr](../xkbase_files/xkbf_init_node_gr.md) |
| 3 | fnodename | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 4 | fconfig | 节点配置（json） | text | 0 |  |  | ' ' | 节点配置（json） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_bf_init_node |  | fid |
| 2 | t_bf_init_node_groupid |  | fgroupid |

---

## 可视化业务流程初始节点-多语言表 t_xk_bf_init_node_l

- **表名称：** 可视化业务流程初始节点-多语言表
- **表名：** t_xk_bf_init_node_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_bf_init_node_l |  | fpkid |
| 2 | idx_t_bf_init_node_l_fid |  | fid |
