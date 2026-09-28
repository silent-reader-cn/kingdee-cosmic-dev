# 合同模板-conm_template

## 附件-附件表 t_conm_attachment

- **表名称：** 附件-附件表
- **表名：** t_conm_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_conm_attachment |  | fpkid |
| 2 | idx_conm_attachment_fentryid |  | fentryid |

---

## 合同模板-主表 t_conm_template

- **表名称：** 合同模板-主表
- **表名：** t_conm_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcontypeid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcontexttype | 合同文本格式 | varchar | 5 |  | √ | ' ' | 合同文本格式 |
| 14 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | furl | 模板URL | varchar | 512 |  |  | null | 模板URL |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fcontentity | 模板适用单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_template_pkey |  | fid |
| 2 | idx_conm_template_number |  | fnumber |

---

## 合同模板-多语言表 t_conm_template_l

- **表名称：** 合同模板-多语言表
- **表名：** t_conm_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_template_l_pkey |  | fpkid |
| 2 | idx_conm_template_l_fid |  | fid,flocaleid |
| 3 | idx_conm_template_l_fname |  | fname,fid |

---

## 组件-子表 t_conm_templateentry

- **表名称：** 组件-子表
- **表名：** t_conm_templateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fismust | 必选 | bpchar | 1 |  | √ | '0' | 必选 |
| 4 | ffieldjson | 字段控制信息 | varchar | 512 |  |  | null | 字段控制信息 |
| 5 | fparamjson | 组件设置信息 | varchar | 512 |  |  | null | 组件设置信息 |
| 6 | fisvisible | 可见性 | bpchar | 1 |  | √ | '0' | 可见性 |
| 7 | fcomponentid | 组件 | int8 | 64 |  | √ | 0 | [合同组件 conm_component](../conm_files/conm_component.md) |
| 8 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 9 | fissys | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 10 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 11 | fparamjson_tag | 组件设置信息_详情 | text | 0 |  |  | null | 组件设置信息_详情 |
| 12 | ffieldjson_tag | 字段控制信息_详情 | text | 0 |  |  | null | 字段控制信息_详情 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_templateentry_pkey |  | fentryid |
| 2 | idx_conm_templateentry_fid |  | fid |

---

## 版本列表-子表 t_conm_attachentry

- **表名称：** 版本列表-子表
- **表名：** t_conm_attachentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenablestatus | 启用状态 | varchar | 5 |  | √ | ' ' | 启用状态 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | ftemplatenum | 模版编码 | varchar | 80 |  | √ | ' ' | 模版编码 |
| 5 | ffilename | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffilemodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fversion | 版本号 | varchar | 80 |  | √ | ' ' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_conm_attachentry |  | fentryid |
| 2 | idx_conm_attachentry_fid |  | fid |

---

## 变量单据体-子表 t_conm_attachsubentry

- **表名称：** 变量单据体-子表
- **表名：** t_conm_attachsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvartype | 变量类型 | varchar | 50 |  | √ | ' ' | 变量类型,枚举: A :文本 B :表格 |
| 2 | fvarnum | 变量编码 | varchar | 100 |  | √ | ' ' | 变量编码 |
| 3 | fsettings_tag | 变量设置_详情 | text | 0 |  |  | null | 变量设置_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fsrcfield | 变量来源 | varchar | 1000 |  | √ | ' ' | 变量来源 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fsettings | 变量设置 | varchar | 512 |  |  | ' ' | 变量设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_attachsubentry |  | fentryid |
| 2 | pk_t_conm_attachsubentry |  | fdetailid |
