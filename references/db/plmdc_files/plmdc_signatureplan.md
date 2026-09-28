# 流程方案配置-plmdc_signatureplan

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
| 10 | fcontrolledsealid | 受控章信息 | int8 | 64 |  | √ | 0 | [受控章信息 plmdc_controlledseal](../plmdc_files/plmdc_controlledseal.md) |
| 11 | fsignconfiguration | 签名配置方式 | varchar | 50 |  | √ | ' ' | 签名配置方式,枚举: bookmark :书签配置 coordinate :坐标配置 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [受控章信息 plmdc_controlledseal](../plmdc_files/plmdc_controlledseal.md) |
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

---

## 发布单接受者方案配置映射-子表 t_plmdc_releflow_relation

- **表名称：** 发布单接受者方案配置映射-子表
- **表名：** t_plmdc_releflow_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecipienttype | 接收者类型 | varchar | 50 |  | √ | ' ' | 接收者类型,枚举: usergroup :用户组 department :部门 role :角色 user :用户 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | frecipientobjid | 接收者对象Id | varchar | 255 |  | √ | ' ' | 接收者对象Id |
| 5 | fopendocright | 打开文档 | bpchar | 1 |  | √ | '0' | 打开文档 |
| 6 | fviewdocright | fviewdocright | bpchar | 1 |  | √ | '1' |  |
| 7 | fdowloaddocright | 下载文档 | bpchar | 1 |  | √ | '0' | 下载文档 |
| 8 | fviewpdfright | 浏览PDF | bpchar | 1 |  | √ | '0' | 浏览PDF |
| 9 | fviewlightright | 浏览轻量化 | bpchar | 1 |  | √ | '0' | 浏览轻量化 |
| 10 | fdowloadstepright | 下载STEP | bpchar | 1 |  | √ | '0' | 下载STEP |
| 11 | fsflownode | 流程节点 | varchar | 50 |  | √ | ' ' | 流程节点 |
| 12 | fsendsubject | 发送主体 | varchar | 50 |  | √ | ' ' | 发送主体,枚举: A :收件人 B :抄送 人 |
| 13 | fsignusers | 接收者 | varchar | 255 |  | √ | ' ' | 接收者 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fdowloadpdfright | 下载PDF | bpchar | 1 |  | √ | '0' | 下载PDF |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_releflow_relation |  | fentryid |
| 2 | idx_plmdc_releflow_relation_fk |  | fid |

---

## 流程方案配置-主表 t_plmdc_signature_config

- **表名称：** 流程方案配置-主表
- **表名：** t_plmdc_signature_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funifiedsign | 统一签字 | bpchar | 1 |  | √ | '0' | 统一签字 |
| 3 | fflowid | 流程 | int8 | 64 |  | √ | 0 | [流程管理 wf_processdefinition](../wf_files/wf_processdefinition.md) |

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

## 发布单单据头方案配置映射-子表 t_plmdc_reflow_relation

- **表名称：** 发布单单据头方案配置映射-子表
- **表名：** t_plmdc_reflow_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhflownode | 流程节点 | varchar | 50 |  | √ | ' ' | 流程节点 |
| 3 | fexpiredatefield | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_reflow_relation |  | fentryid |
| 2 | idx_plmdc_reflow_relation1_fk |  | fid |

---

## 流程坐标配置映射-子表 t_plmdc_signflow_postion

- **表名称：** 流程坐标配置映射-子表
- **表名：** t_plmdc_signflow_postion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfiguration | 配置内容 | varchar | 50 |  | √ | ' ' | 配置内容,枚举: signbook :签名书签 datebook :日期书签 auditbook :审批意见书签 docrevbook :文档版本书签 stampsignbook :签章书签 |
| 3 | fdrawing | 图纸方向 | varchar | 50 |  | √ | ' ' | 图纸方向,枚举: horizontal :横向 vertical :纵向 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fwidth | 宽度 | numeric | 23 | 2 | √ | 0 | 宽度 |
| 6 | fpflownode | 流程节点 | varchar | 50 |  | √ | ' ' | 流程节点 |
| 7 | fx | X轴 | numeric | 23 | 2 | √ | 0 | X轴 |
| 8 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: PDF :PDF Solidworks :Solidworks Creo :Creo Catia :Catia UG :UG Autocad :Autocad 中望2D :中望2D |
| 9 | fy | Y轴 | numeric | 23 | 2 | √ | 0 | Y轴 |
| 10 | fscale | 缩放比例 | numeric | 23 | 2 | √ | 0 | 缩放比例 |
| 11 | fheight | 高度 | numeric | 23 | 2 | √ | 0 | 高度 |
| 12 | ftabsize | 页面大小 | varchar | 50 |  | √ | ' ' | 页面大小,枚举: a4 :a4 a3 :a3 a2 :a2 a1 :a1 a0 :a0 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_signflow_postion |  | fid |
| 2 | pk_t_plmdc_signflow_postion |  | fentryid |
