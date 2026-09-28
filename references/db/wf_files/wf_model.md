# 流程设计-wf_model

## 流程设计-多语言表 t_wf_model_l

- **表名称：** 流程设计-多语言表
- **表名：** t_wf_model_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 1024 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 3000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_model_l_pkey |  | fpkid |
| 2 | idx_wf_model_localeid |  | fid,flocaleid |

---

## 流程设计-主表 t_wf_model

- **表名称：** 流程设计-主表
- **表名：** t_wf_model

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemplatenumber | 流程模板编码 | varchar | 50 |  | √ | ' ' | 流程模板编码 |
| 3 | fdeploymentid | 部署ID | int8 | 64 |  | √ | 0 | 部署ID |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbusinessid | 流程标识 | varchar | 255 |  | √ | ' ' | 流程标识 |
| 6 | ftemplateversion | 流程模板版本 | int4 | 32 |  | √ | 0 | 流程模板版本 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 8 | fapplicationid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 11 | fpublish | 是否发布 | bpchar | 1 |  | √ | '0' | 是否发布 |
| 12 | foperation | 启动操作 | varchar | 300 |  | √ | ' ' | 启动操作 |
| 13 | fentrabillid | 入口单据ID | varchar | 36 |  | √ | ' ' | 实体元数据 bos_entitymeta |
| 14 | fversion | 版本 | varchar | 36 |  | √ | ' ' | 版本 |
| 15 | fentrabill | 单据 | varchar | 36 |  | √ | ' ' | 单据 |
| 16 | forgunitid | 所属组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 18 | fname | 名称 | varchar | 1024 |  | √ | ' ' | 名称 |
| 19 | fcategory | 类别ID | int8 | 64 |  | √ | 0 | 流程分类 wf_processcagetory |
| 20 | ftemplateid | 流程模板 | int8 | 64 |  | √ | 0 | 流程模板 wf_proctemplate |
| 21 | fdescription | 描述 | varchar | 3000 |  | √ | ' ' | 描述 |
| 22 | fgraphid | 设计器图形ID | int8 | 64 |  | √ | 0 | 设计器图形ID |
| 23 | fdiscard | 是否废弃 | bpchar | 1 |  | √ | '0' | 是否废弃 |
| 24 | fpngid | 流程SVG资源ID | int8 | 64 |  | √ | 0 | 流程SVG资源ID |
| 25 | ftype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 26 | fparentprocid | 父流程ID | int8 | 64 |  | √ | 0 | 父流程ID |
| 27 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 28 | fbpmnxmlid | BPMNXMLID | int8 | 64 |  | √ | 0 | BPMNXMLID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_model_number |  | fnumber |
| 2 | t_wf_model_pkey |  | fid |
