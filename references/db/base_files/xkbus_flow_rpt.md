# 可视化业务流程报表-xkbus_flow_rpt

## 可视化业务流程报表-多语言表 t_xk_bus_flow_rpt_l

- **表名称：** 可视化业务流程报表-多语言表
- **表名：** t_xk_bus_flow_rpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_bus_flow_rpt_l |  | fpkid |
| 2 | idx_t_bf_rpt_l_fid |  | fid |

---

## 可视化业务流程报表-主表 t_xk_bus_flow_rpt

- **表名称：** 可视化业务流程报表-主表
- **表名：** t_xk_bus_flow_rpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbusflowid | 业务流程 | int8 | 64 |  | √ | 0 | [可视化业务流程 xkbus_flow](../xkbase_files/xkbus_flow.md) |
| 5 | fconfig | 配置数据（json） | text | 0 |  |  | ' ' | 配置数据（json） |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: RPT :报表 BD :基础资料 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bf_rpt_flowid |  | fbusflowid |
| 2 | pk_t_xk_bus_flow_rpt |  | fid |
