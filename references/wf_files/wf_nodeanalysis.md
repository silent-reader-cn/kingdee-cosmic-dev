# 节点效率分析统计-wf_nodeanalysis

## 节点效率分析统计-主表 t_wf_nodeanalysis

- **表名称：** 节点效率分析统计-主表
- **表名：** t_wf_nodeanalysis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgunitid | 组织ID | int8 | 64 |  | √ | 0 | 组织ID |
| 3 | fnodetype | 节点类型 | varchar | 100 |  | √ | ' ' | 节点类型 |
| 4 | fmaxduration | 最长耗时 | int8 | 64 |  | √ | 0 | 最长耗时 |
| 5 | fschemeid | 流程方案ID | int8 | 64 |  | √ | 0 | 流程方案ID |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码 |
| 8 | ftotalduration | 总耗时 | int8 | 64 |  | √ | 0 | 总耗时 |
| 9 | fentityname | 实体名称 | varchar | 115 |  | √ | ' ' | 实体名称 |
| 10 | ftotalrealduration | 真实总耗时 | int8 | 64 |  | √ | 0 | 真实总耗时 |
| 11 | fnodetypename | 节点类型名称 | varchar | 50 |  | √ | ' ' | 节点类型名称 |
| 12 | fnodename | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 13 | fyears | 年月 | varchar | 10 |  | √ | ' ' | 年月 |
| 14 | fproctype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 15 | fnodeid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 16 | finstancecount | 任务实例数/执行次数 | int4 | 32 |  | √ | 0 | 任务实例数/执行次数 |
| 17 | fprocname | 流程名称 | varchar | 115 |  | √ | ' ' | 流程名称 |
| 18 | fprocnumber | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 19 | fmaxrealduration | 最长真实耗时 | int8 | 64 |  | √ | 0 | 最长真实耗时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_nodeanalysis |  | fid |
| 2 | idx_wf_nodeanaly_nodetype |  | fnodetype |
| 3 | idx_wf_nodeanaly_org |  | forgunitid |
| 4 | idx_wf_nodeanaly_nodeid |  | fnodeid |
| 5 | idx_wf_nodeanaly_proctype |  | fproctype |
| 6 | idx_wf_nodeanaly_years |  | fyears |
| 7 | idx_wf_nodeanaly_entity |  | fentitynumber |
| 8 | idx_wf_nodeanaly_procdef |  | fprocdefid |

---

## 节点效率分析统计-多语言表 t_wf_nodeanalysis_l

- **表名称：** 节点效率分析统计-多语言表
- **表名：** t_wf_nodeanalysis_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名称 | varchar | 115 |  | √ | ' ' | 实体名称 |
| 3 | fnodetypename | 节点类型名称 | varchar | 500 |  | √ | ' ' | 节点类型名称 |
| 4 | fnodename | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 5 | fprocname | 流程名称 | varchar | 115 |  | √ | ' ' | 流程名称 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nodeanalysis_l |  | fid,flocaleid |
| 2 | pk_t_wf_nodeanalysis_l |  | fpkid |
| 3 | idx_wf_nodeanaly_l_procname |  | fprocname |
| 4 | idx_wf_nodeanaly_l_nodename |  | fnodename |
