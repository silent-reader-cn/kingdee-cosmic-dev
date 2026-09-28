# 单据流程配置-pds_billflow

## 关键流程分录-子表 t_pds_billnode

- **表名称：** 关键流程分录-子表
- **表名：** t_pds_billnode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbiznodeid | 关键业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 5 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 6 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已关闭 Z :无需处理 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_billnode |  | fentryid |
| 2 | idx_pds_billnode_fid |  | fid |

---

## 附属流程分录-子表 t_pds_billnodesub

- **表名称：** 附属流程分录-子表
- **表名：** t_pds_billnodesub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbiznodeid | 附属业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 2 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已关闭 Z :无需处理 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 8 | fisaudit | 是否需要审核 | bpchar | 1 |  | √ | '0' | 是否需要审核 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_billnodesub |  | fentryid |
| 2 | idx_pds_billnodesub_fid |  | fdetailid |

---

## 单据流程配置-主表 t_pds_billflow

- **表名称：** 单据流程配置-主表
- **表名：** t_pds_billflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillid | 单据ID | varchar | 50 |  | √ | ' ' | 单据ID |
| 3 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_billflow |  | fid |
| 2 | idx_pds_billflow_bid |  | fbillid |
