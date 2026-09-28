# 智能体推荐方案-er_agent_recommendplan

## 单据体-子表 t_er_recomplandetail

- **表名称：** 单据体-子表
- **表名：** t_er_recomplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentnumber | 智能体编码 | varchar | 50 |  | √ | ' ' | 智能体编码 |
| 3 | fisbook | 已预订 | bpchar | 1 |  | √ | '0' | 已预订 |
| 4 | fentrystatus | 智能体状态 | bpchar | 1 |  | √ | '0' | 智能体状态,枚举: 0 :未开始 1 :执行完成 2 :异常 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fagentvalue | agentvalue | varchar | 255 |  | √ | ' ' | agentvalue |
| 7 | fagentvalue_tag | agentvalue_详情 | text | 0 |  |  | null | agentvalue_详情 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_recomplandetail |  | fentryid |

---

## 智能体推荐方案-主表 t_er_recommendplan

- **表名称：** 智能体推荐方案-主表
- **表名：** t_er_recommendplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftripinfo | 出差信息 | varchar | 2000 |  | √ | ' ' | 出差信息 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsessionid | sessionid | varchar | 100 |  | √ | ' ' | sessionid |
| 5 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 6 | fschemetype | 方案类型 | varchar | 50 |  | √ | 'tripCard' | 方案类型,枚举: tripCard :差旅 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_recommendplan |  | fid |

---

## 单据体-子表 t_er_recomplanorder

- **表名称：** 单据体-子表
- **表名：** t_er_recomplanorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fordernum | 订单号 | varchar | 255 |  | √ | ' ' | 订单号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fagententryid | 智能体推荐分录ID | int8 | 64 |  | √ | 0 | 智能体推荐分录ID |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recomplanorder_fordernum |  | fordernum |
| 2 | pk_er_recomplanorder |  | fentryid |
