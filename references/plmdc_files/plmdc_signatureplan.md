# 签字方案配置-plmdc_signatureplan

## 签字方案配置-主表 t_plmdc_signature_config

- **表名称：** 签字方案配置-主表
- **表名：** t_plmdc_signature_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funifiedsign | 统一签字 | bpchar | 1 |  | √ | '0' | 统一签字 |
| 3 | fflowid | 流程 | int8 | 64 |  | √ | 0 | 流程管理 wf_processdefinition |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_signcof_flowid |  | fflowid |
| 2 | pk_t_plmdc_signature_config |  | fid |

---

## 流程方案配置映射-子表 t_plmdc_signflow_relation

- **表名称：** 流程方案配置映射-子表
- **表名：** t_plmdc_signflow_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdateformat | 日期格式 | varchar | 255 |  | √ | ' ' | 日期格式,枚举: YYYY-MM-dd :YYYY-MM-dd |
| 3 | fsignbookmark | 签名书签 | varchar | 255 |  | √ | ' ' | 签名书签 |
| 4 | fdocrevbookmark | 文档版本书签 | varchar | 255 |  | √ | ' ' | 文档版本书签 |
| 5 | fstampsignbookmark | 签章书签 | varchar | 255 |  | √ | ' ' | 签章书签 |
| 6 | fdatebookmark | 日期书签 | varchar | 255 |  | √ | ' ' | 日期书签 |
| 7 | fauditbookmark | 审批意见书签 | varchar | 255 |  | √ | ' ' | 审批意见书签 |
| 8 | fflownodeid | 流程节点 | varchar | 255 |  | √ | ' ' | 流程节点 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fcontrolledsealid | 受控章信息 | int8 | 64 |  | √ | 0 | 受控章信息 plmdc_controlledseal |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_signflow_relation |  | fentryid |
| 2 | idx_plmdc_signflow_fid |  | fid |

---

## 受控章-多选基础资料表 t_plmdc_multicontrolledse

- **表名称：** 受控章-多选基础资料表
- **表名：** t_plmdc_multicontrolledse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 受控章信息 plmdc_controlledseal |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_multicontrolledse |  | fpkid |
| 2 | idx_plmdc_mulctr_fentryid |  | fentryid |
