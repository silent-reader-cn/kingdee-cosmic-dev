# 分析中心流程过滤列表-wf_processes

## 分析中心流程过滤列表-多语言表 t_wf_procdef_l

- **表名称：** 分析中心流程过滤列表-多语言表
- **表名：** t_wf_procdef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fversiondesc | 版本描述 | varchar | 255 |  | √ | ' ' | 版本描述 |
| 4 | fpublishname | 发布人 | varchar | 230 |  | √ | ' ' | 发布人 |
| 5 | fcategoryname | 类别名称 | varchar | 115 |  | √ | ' ' | 类别名称 |
| 6 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 7 | fdescription | 描述 | varchar | 3000 |  | √ | ' ' | 描述 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_procdef_localeid |  | fid,flocaleid |
| 2 | t_wf_procdef_l_pkey |  | fpkid |

---

## 分析中心流程过滤列表-主表 t_wf_procdef

- **表名称：** 分析中心流程过滤列表-主表
- **表名：** t_wf_procdef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpublishname | 发布人 | varchar | 230 |  | √ | ' ' | 发布人 |
| 3 | fmodelid | 模型ID | int8 | 64 |  | √ | 0 | 模型ID |
| 4 | fcategoryname | 类别名称 | varchar | 115 |  | √ | ' ' | 类别名称 |
| 5 | fengineversion | 引擎版本 | varchar | 36 |  | √ | ' ' | 引擎版本 |
| 6 | fdeploymentid | 部署ID | int8 | 64 |  | √ | 0 | 部署ID |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbusinessid | 流程标识 | varchar | 255 |  | √ | ' ' | 流程标识 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 10 | fapplicationid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 11 | fcategorynumber | 类别编码 | varchar | 50 |  | √ | ' ' | 类别编码 |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 14 | fkey | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 15 | fcategoryid | 类别ID | int8 | 64 |  | √ | 0 | 类别ID |
| 16 | foperation | 绑定操作 | varchar | 300 |  | √ | ' ' | 绑定操作 |
| 17 | fentrabillid | 入口单据 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 18 | fversion | 版本 | varchar | 36 |  | √ | ' ' | 版本 |
| 19 | fentrabill | 入口单据编码 | varchar | 36 |  | √ | ' ' | 入口单据编码 |
| 20 | ftemplate | 模板 | varchar | 100 |  | √ | ' ' | 模板 |
| 21 | forgunitid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 23 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 24 | fversiondesc | 版本描述 | varchar | 255 |  | √ | ' ' | 版本描述 |
| 25 | fallowmodification | 是否允许修改 | bpchar | 1 |  | √ | '1' | 是否允许修改 |
| 26 | fresourceid | 模型资源ID | int8 | 64 |  | √ | 0 | 模型资源ID |
| 27 | fgraphname | 流程图片资源名 | varchar | 80 |  | √ | ' ' | 流程图片资源名 |
| 28 | fdescription | 描述 | varchar | 3000 |  | √ | ' ' | 描述 |
| 29 | fversionstate | 版本状态 | varchar | 50 |  | √ | ' ' | 版本状态,枚举: newest :最新版 historical :历史版 |
| 30 | fgraphicaldefined | 是否已生成图形 | bpchar | 1 |  | √ | '0' | 是否已生成图形 |
| 31 | ftype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 32 | fparentprocid | 父流程ID | int8 | 64 |  | √ | 0 | 父流程ID |
| 33 | fenable | 启用状态 | varchar | 30 |  | √ | ' ' | 启用状态,枚举: enable :启用 disable :禁用 |
| 34 | fprimarysubprocess | 子流程 | varchar | 30 |  | √ | ' ' | 子流程,枚举: sub :子流程 main :主流程 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_procdef_number |  | fkey |
| 2 | t_wf_procdef_pkey |  | fid |
| 3 | idx_wf_procdef_entrabill |  | fentrabill |
| 4 | idx_wf_procdef_modelid |  | fmodelid |
| 5 | idx_wf_procdef_enable |  | fenable |
| 6 | idx_wf_procdef_type |  | ftype |
