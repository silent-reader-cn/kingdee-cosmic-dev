# 模板管理-plm_importtemplate

## 模板管理-多语言表 t_plmsm_init_template_l

- **表名称：** 模板管理-多语言表
- **表名：** t_plmsm_init_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_init_template_l |  | fid |
| 2 | pk_t_plmsm_init_template_l |  | fpkid |

---

## 模板管理-主表 t_plmsm_init_template

- **表名称：** 模板管理-主表
- **表名：** t_plmsm_init_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenableimport | 允许引入引出 | varchar | 50 |  | √ | ' ' | 允许引入引出 |
| 3 | fapplyscope | 模板适用范围 | varchar | 50 |  | √ | ' ' | 模板适用范围,枚举: 0 :全局共用 1 :指定使用人 |
| 4 | ftemplatetype | 模板类型 | varchar | 50 |  | √ | ' ' | 模板类型,枚举: IMPT :引入模板 EXPT :引出模板 |
| 5 | ftemplateurl | 模板url | varchar | 255 |  | √ | ' ' | 模板url |
| 6 | fispreset | 预置模板 | bpchar | 1 |  | √ | '0' | 预置模板 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsplitsubentries | 启用模板参数“#SplitSubEntries” | bpchar | 1 |  | √ | '0' | 启用模板参数“#SplitSubEntries” |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fplugin | 插件 | varchar | 2000 |  | √ | ' ' | 插件 |
| 13 | fenablesetnull | 启用模板参数“#SetNULL” | bpchar | 1 |  | √ | '1' | 启用模板参数“#SetNULL” |
| 14 | fforupdatemultilangfields | 启用模板参数“#ForUpdateMultiLangFields” | bpchar | 1 |  | √ | '0' | 启用模板参数“#ForUpdateMultiLangFields” |
| 15 | fapplylayout | 模板适用布局 | varchar | 255 |  | √ | ' ' | 模板适用布局,枚举: |
| 16 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ffolderid | 所属文件夹 | int8 | 64 |  | √ | 0 | 系统文件夹 plm_pdm_folder_hub |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | PLM引入模板实体对象 plm_entityobject |
| 21 | fexchangenameandmark | 互换字段名称和备注 | bpchar | 1 |  | √ | '0' | 互换字段名称和备注 |
| 22 | fhidefieldrow | 隐藏字段标识行 | bpchar | 1 |  | √ | '0' | 隐藏字段标识行 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 25 | ftemplateurl_tag | 模板url_详情 | text | 0 |  |  | null | 模板url_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_init_template_number |  | fnumber |
| 2 | pk_t_plmsm_init_template |  | fid |

---

## 附件面板选择单据体-子表 t_plm_init_template_att

- **表名称：** 附件面板选择单据体-子表
- **表名：** t_plm_init_template_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fatt_isinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 3 | fatt_isimport | 是否引入 | bpchar | 1 |  | √ | '0' | 是否引入 |
| 4 | fattdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | fatt_colwidth | Excel字段列宽 | int4 | 32 |  | √ | 0 | Excel字段列宽 |
| 8 | fatt_number | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_init_template_att_fid |  | fid |
| 2 | pk_t_plm_init_template_att |  | fentryid |

---

## 模板说明-附件表 t_plmsm_imptemplateattach

- **表名称：** 模板说明-附件表
- **表名：** t_plmsm_imptemplateattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_imptemplateattach |  | fpkid |
| 2 | idx_plmsm_imptemplateatt_fid |  | fid |

---

## 字段选择-子表 t_plmsm_inittemplateentry

- **表名称：** 字段选择-子表
- **表名：** t_plmsm_inittemplateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcename | 源实体 | varchar | 50 |  | √ | ' ' | 源实体 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdescription | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | ffieldkey | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 6 | fmustinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 7 | fexportformat | 引出格式 | varchar | 50 |  | √ | ' ' | 引出格式 |
| 8 | fisdate | 是否日期 | bpchar | 1 |  | √ | '0' | 是否日期 |
| 9 | fimportprop | 引入属性 | varchar | 50 |  | √ | ' ' | 引入属性,枚举: number :编码 name :名称 id :内码 |
| 10 | fisimport | 是否允许引入引出 | bpchar | 1 |  | √ | '0' | 是否允许引入引出 |
| 11 | fisfield | 是否字段 | bpchar | 1 |  | √ | '0' | 是否字段 |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 13 | fcolwidth | Excel字段列宽 | int8 | 64 |  | √ | 0 | Excel字段列宽 |
| 14 | fsourceentity | 源实体标识 | varchar | 50 |  | √ | ' ' | 源实体标识 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fexportprop | 引出属性 | varchar | 255 |  | √ | ' ' | 引出属性 |
| 17 | fexportformatname | 引出格式 | varchar | 50 |  | √ | ' ' | 引出格式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_templateentry |  | fid |
| 2 | pk_t_plmsm_inittemplateentry |  | fentryid |

---

## 使用人-多选基础资料表 t_plmsm_imptemplateusers

- **表名称：** 使用人-多选基础资料表
- **表名：** t_plmsm_imptemplateusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_templateusers_fid |  | fid |
| 2 | pk_plmsm_imptemplateusers |  | fpkid |

---

## 附件面板选择单据体-多语言表 t_plm_init_template_att_l

- **表名称：** 附件面板选择单据体-多语言表
- **表名：** t_plm_init_template_att_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fattdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_template_att__l_fentryid |  | fentryid |
| 2 | pk_t_plm_init_template_att_l |  | fpkid |
