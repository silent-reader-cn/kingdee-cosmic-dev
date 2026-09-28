# 流程效率分析统计-wf_procanalysis

## 流程效率分析统计-多语言表 t_wf_procanalysis_l

- **表名称：** 流程效率分析统计-多语言表
- **表名：** t_wf_procanalysis_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名称 | varchar | 115 |  | √ | ' ' | 实体名称 |
| 3 | fprocname | 流程名称 | varchar | 115 |  | √ | ' ' | 流程名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_procanalysis_l |  | fid,flocaleid |
| 2 | idx_wf_procanaly_l_procname |  | fprocname |
| 3 | pk_t_wf_procanalysis_l |  | fpkid |

---

## 流程效率分析统计-主表 t_wf_procanalysis

- **表名称：** 流程效率分析统计-主表
- **表名：** t_wf_procanalysis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgunitid | 组织ID | int8 | 64 |  | √ | 0 | 组织ID |
| 3 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 4 | fprocdefid | 流程定义 | int8 | 64 |  | √ | 0 | 流程定义 |
| 5 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码 |
| 6 | ftotalduration | 总耗时 | int8 | 64 |  | √ | 0 | 总耗时 |
| 7 | fentityname | 实体名称 | varchar | 115 |  | √ | ' ' | 实体名称 |
| 8 | ftotalrealduration | 真实总耗时 | int8 | 64 |  | √ | 0 | 真实总耗时 |
| 9 | fyears | 年月 | varchar | 10 |  | √ | ' ' | 年月 |
| 10 | fproctype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 11 | finstancecount | 处理实例数 | int4 | 32 |  | √ | 0 | 处理实例数 |
| 12 | fprocname | 流程名称 | varchar | 115 |  | √ | ' ' | 流程名称 |
| 13 | fprocnumber | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 14 | fprocversion | 流程版本 | varchar | 36 |  | √ | ' ' | 流程版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_procanaly_proctype |  | fproctype |
| 2 | idx_wf_procanaly_entity |  | fentitynumber |
| 3 | idx_wf_procanaly_procnumber |  | fprocnumber |
| 4 | idx_wf_procanaly_procdef |  | fprocdefid |
| 5 | idx_wf_procanaly_years |  | fyears |
| 6 | idx_wf_procanaly_org |  | forgunitid |
| 7 | pk_t_wf_procanalysis |  | fid |
