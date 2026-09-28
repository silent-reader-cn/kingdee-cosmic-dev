# 引入引出模板-bos_importtemplate

## 字段选择-子表 t_bas_importtemplateentry

- **表名称：** 字段选择-子表
- **表名：** t_bas_importtemplateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | ffieldname | varchar | 50 |  |  | null |  |
| 3 | fsourcename | 源实体 | varchar | 255 |  | √ | ' ' | 源实体 |
| 4 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 5 | fdescription | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 6 | ffieldkey | 编码 | varchar | 50 |  |  | null | 编码 |
| 7 | fmustinput | 是否必录 | bpchar | 1 |  |  | null | 是否必录 |
| 8 | fexportformat | 引出格式 | varchar | 50 |  | √ | ' ' | 引出格式 |
| 9 | fisdate | 是否日期 | bpchar | 1 |  | √ | ' ' | 是否日期 |
| 10 | fimportprop | 引入属性 | varchar | 36 |  |  | null | 引入属性,枚举: number :编码 name :名称 id :内码 |
| 11 | fisimport | 是否允许引入引出 | bpchar | 1 |  |  | null | 是否允许引入引出 |
| 12 | fisfield | 是否字段 | bpchar | 1 |  |  | null | 是否字段 |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 14 | fcolwidth | Excel字段列宽 | int4 | 32 |  | √ | 0 | Excel字段列宽 |
| 15 | fsourceentity | 源实体标识 | varchar | 255 |  | √ | ' ' | 源实体标识 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fexportprop | 引出属性 | varchar | 255 |  | √ | ' ' | 引出属性 |
| 18 | fexportformatname | 引出格式 | varchar | 50 |  | √ | ' ' | 引出格式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_importtemplateentry_pkey |  | fentryid |
| 2 | idx_bas_importtemplateentry_id |  | fid |

---

## 引入引出模板-主表 t_bas_importtemplate

- **表名称：** 引入引出模板-主表
- **表名：** t_bas_importtemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 4 | fcomment | fcomment | varchar | 500 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fenableimport | 允许引入引出 | varchar | 100 |  | √ | ' ' | 允许引入引出 |
| 8 | fapplyscope | 模板适用范围 | bpchar | 1 |  | √ | '0' | 模板适用范围,枚举: 0 :全局共用 1 :指定使用人 |
| 9 | ftemplatetype | 模板类型 | varchar | 36 |  |  | null | 模板类型,枚举: IMPT :引入模板 EXPT :引出模板 |
| 10 | fispreset | 预置模板 | bpchar | 1 |  | √ | '0' | 预置模板 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fexchangenameandmark | 互换字段名称和备注 | bpchar | 1 |  | √ | '0' | 互换字段名称和备注 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fsplitsubentries | 启用模板参数“#SplitSubEntries” | bpchar | 1 |  | √ | '0' | 启用模板参数“#SplitSubEntries” |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fhidefieldrow | 隐藏字段标识行 | bpchar | 1 |  | √ | '0' | 隐藏字段标识行 |
| 18 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fplugin | 插件 | varchar | 2000 |  | √ | ' ' | 插件 |
| 20 | fnumber | 编码 | varchar | 50 |  |  | null | 编码 |
| 21 | fenablesetnull | 启用模板参数“#SetNULL” | bpchar | 1 |  | √ | '1' | 启用模板参数“#SetNULL” |
| 22 | fforupdatemultilangfields | 启用模板参数“#ForUpdateMultiLangFields” | bpchar | 1 |  | √ | '0' | 启用模板参数“#ForUpdateMultiLangFields” |
| 23 | foverrideentry | foverrideentry | bpchar | 1 |  | √ | '0' |  |
| 24 | fapplylayout | 模板适用布局 | varchar | 255 |  | √ | ' ' | 模板适用布局,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_importtemplate |  | fnumber |
| 2 | t_bas_importtemplate_pkey |  | fid |

---

## 附件面板选择单据体-多语言表 t_bas_importtemplate_att_l

- **表名称：** 附件面板选择单据体-多语言表
- **表名：** t_bas_importtemplate_att_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fattdescription | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_importtemplate_att_l |  | fpkid |

---

## 使用人-多选基础资料表 t_bas_imptemplateusers

- **表名称：** 使用人-多选基础资料表
- **表名：** t_bas_imptemplateusers

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
| 1 | idx_bas_imptemplateusers_id |  | fid,fbasedataid |
| 2 | pk_bas_imptemplateusers |  | fpkid |

---

## 模板说明-附件表 t_bas_imptemplateattach

- **表名称：** 模板说明-附件表
- **表名：** t_bas_imptemplateattach

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
| 1 | pk_bas_imptemplateattach |  | fpkid |
| 2 | idx_bas_imptemplateattach_id |  | fid,fbasedataid |

---

## 引入引出模板-多语言表 t_bas_importtemplate_l

- **表名称：** 引入引出模板-多语言表
- **表名：** t_bas_importtemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fcomment | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_importtemplate_l |  | fid,flocaleid |
| 2 | t_bas_importtemplate_l_pkey |  | fpkid |

---

## 附件面板选择单据体-子表 t_bas_importtemplate_att

- **表名称：** 附件面板选择单据体-子表
- **表名：** t_bas_importtemplate_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fatt_isinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 3 | fatt_isimport | 是否引入 | bpchar | 1 |  | √ | '0' | 是否引入 |
| 4 | fattdescription | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fatt_colwidth | Excel字段列宽 | int8 | 64 |  |  | null | Excel字段列宽 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fatt_number | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_importtemplate_att |  | fentryid |
