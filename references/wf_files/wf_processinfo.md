# 流程批量设置-wf_processinfo

## 流程批量设置-主表 t_wf_processinfo

- **表名称：** 流程批量设置-主表
- **表名：** t_wf_processinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresourceid | 资源ID | int8 | 64 |  | √ | 0 | 资源ID |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fschemeid | 流程方案 | int8 | 64 |  | √ | 0 | 流程动态方案配置 wf_processdynamicconfig |
| 5 | fprocdefid | 流程定义 | int8 | 64 |  | √ | 0 | 流程管理 wf_processdefinition |
| 6 | fprocesstype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 7 | fentityid | 流程单据 | varchar | 36 |  | √ | ' ' | 实体元数据 bos_entitymeta |
| 8 | fschemetype | 方案类型 | varchar | 15 |  | √ | ' ' | 方案类型,枚举: default :默认方案 custom :自定义方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_processinfo |  | fid |
| 2 | idx_wf_processinfo_procdef |  | fprocdefid |
| 3 | idx_wf_processinfo_scheme |  | fschemeid |

---

## 单据体-子表 t_wf_processinfodetail

- **表名称：** 单据体-子表
- **表名：** t_wf_processinfodetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factivitytemplateid | 节点模板ID | int8 | 64 |  | √ | 0 | 节点模板ID |
| 3 | factivitynumber | 节点编码 | varchar | 50 |  | √ | ' ' | 节点编码 |
| 4 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 5 | factivitytype | 节点类型 | varchar | 50 |  | √ | ' ' | 节点类型 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | factivityid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | factivityentityid | 节点单据 | varchar | 36 |  | √ | ' ' | 实体元数据 bos_entitymeta |
| 10 | factivitytypename | 节点类型名称 | varchar | 50 |  | √ | ' ' | 节点类型名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_processinfodetail |  | fid |
| 2 | pk_t_wf_processinfodetail |  | fentryid |

---

## 单据体-多语言表 t_wf_processinfodetail_l

- **表名称：** 单据体-多语言表
- **表名：** t_wf_processinfodetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | factivitytypename | 节点类型名称 | varchar | 50 |  | √ | ' ' | 节点类型名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_processinfodetail_l |  | fentryid,flocaleid |
| 2 | pk_t_wf_processinfodetail_l |  | fpkid |
