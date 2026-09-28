# 文件类型-plm_plmdc_file_type

## 明细栏数据对应关系单据体-多语言表 t_plmdc_detail_mapping_l

- **表名称：** 明细栏数据对应关系单据体-多语言表
- **表名：** t_plmdc_detail_mapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fmatpropertyname | 物料字段多语言 | varchar | 50 |  | √ | ' ' | 物料字段多语言 |
| 5 | fpropertyname | 文档字段多语言 | varchar | 50 |  | √ | ' ' | 文档字段多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_detail_mapping_l_fk |  | fentryid |
| 2 | pk_t_plmdc_detail_mapping_l |  | fpkid |

---

## 绑定物料业务模型-多选基础资料表 t_plmdc_filetype_matmodel

- **表名称：** 绑定物料业务模型-多选基础资料表
- **表名：** t_plmdc_filetype_matmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_filetype_matmodel |  | fentryid |
| 2 | pk_t_plmdc_filetype_matmodel |  | fpkid |

---

## 文件类型-主表 t_plmdc_file_type

- **表名称：** 文件类型-主表
- **表名：** t_plmdc_file_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 文件类型名称 | varchar | 50 |  | √ | ' ' | 文件类型名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fdoctype | 文档类别 | varchar | 50 |  | √ | ' ' | 文档类别,枚举: A :普通 B :2D C :3D D :电子 E :电气 |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 文件类型编码 | varchar | 30 |  | √ | ' ' | 文件类型编码 |
| 20 | ffileextension | ffileextension | varchar | 50 |  | √ | ' ' |  |
| 21 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmdc_file_type_master |  | fmasterid |
| 2 | pk_plmdc_file_type |  | fid |
| 3 | idx_plmdc_file_type_number |  | fnumber |
| 4 | idx_t_plmdc_file_type_createorg |  | fcreateorgid |

---

## 数据对应关系单据体-多语言表 t_plmdc_filetype_mapping_l

- **表名称：** 数据对应关系单据体-多语言表
- **表名：** t_plmdc_filetype_mapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fmatpropertyname | 物料字段多语言 | varchar | 50 |  | √ | ' ' | 物料字段多语言 |
| 5 | fpropertyname | 文档字段多语言 | varchar | 50 |  | √ | ' ' | 文档字段多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_filetype_mapping_l_fk |  | fentryid |
| 2 | pk_t_plmdc_filetype_mapping_l |  | fpkid |

---

## 文件类型-使用范围表 t_plmdc_file_type_u

- **表名称：** 文件类型-使用范围表
- **表名：** t_plmdc_file_type_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmdc_file_type_u_uo |  | fuseorgid |
| 2 | pk_t_plmdc_file_type_u |  | fdataid,fuseorgid |

---

## 数据对应关系单据体-子表 t_plmdc_filetype_mapping

- **表名称：** 数据对应关系单据体-子表
- **表名：** t_plmdc_filetype_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdocumentfield | 物理文件字段 | varchar | 50 |  | √ | ' ' | 物理文件字段 |
| 3 | findex | 物料索引 | bpchar | 1 |  | √ | '0' | 物料索引 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 6 | fmetadatajson | 元数据信息json | varchar | 255 |  | √ | ' ' | 元数据信息json |
| 7 | fmodelpropertycode | fmodelpropertycode | varchar | 50 |  | √ | ' ' |  |
| 8 | fmatmustinput | 物料是否必填 | varchar | 50 |  | √ | ' ' | 物料是否必填 |
| 9 | fedocumentfield | 物理文件字段 | int8 | 64 |  | √ | 0 | EPLAN属性 plm_plmdc_eplan_attr |
| 10 | fmatpropertyname | 物料字段多语言 | varchar | 50 |  | √ | ' ' | 物料字段多语言 |
| 11 | fmatpropertycode | 物料字段属性编码 | varchar | 50 |  | √ | ' ' | 物料字段属性编码 |
| 12 | fmustinput | 文档是否必填 | varchar | 50 |  | √ | ' ' | 文档是否必填 |
| 13 | ffieldtype | 字段类别 | varchar | 50 |  | √ | ' ' | 字段类别,枚举: ModelField :模型属性 ClassifyField :分类属性 |
| 14 | fmodelpropertyname | fmodelpropertyname | varchar | 50 |  | √ | ' ' |  |
| 15 | fmetadatajson_tag | 元数据信息json_详情 | text | 0 |  |  | null | 元数据信息json_详情 |
| 16 | fepropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: NORMAL :一般字段 BOM :BOM字段 |
| 17 | fdocumentindex | 文件索引 | bpchar | 1 |  | √ | '0' | 文件索引 |
| 18 | fpropertycode | 文档字段编码 | varchar | 50 |  | √ | ' ' | 文档字段编码 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fpropertyname | 文档字段多语言 | varchar | 50 |  | √ | ' ' | 文档字段多语言 |
| 21 | fmaterialmodel | 模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 22 | fmaterialclass | 分类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_filetype_mapping_fk |  | fid |
| 2 | pk_t_plmdc_filetype_mapping |  | fentryid |

---

## 文件类型-多语言表 t_plmdc_file_type_l

- **表名称：** 文件类型-多语言表
- **表名：** t_plmdc_file_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 文件类型名称 | varchar | 50 |  | √ | ' ' | 文件类型名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_file_type_l_0 |  | fid,flocaleid |
| 2 | pk_plmdc_file_type_l |  | fpkid |

---

## 文件扩展名单据体-多语言表 t_plmdc_filetype_entry_l

- **表名称：** 文件扩展名单据体-多语言表
- **表名：** t_plmdc_filetype_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_filetype_entry_l |  | fpkid |
| 2 | idx_plm_filetype_entry_l_fk |  | fentryid |

---

## 明细栏数据对应关系单据体-子表 t_plmdc_detail_mapping

- **表名称：** 明细栏数据对应关系单据体-子表
- **表名：** t_plmdc_detail_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvirtualdocumentname | 虚文档名称 | bpchar | 1 |  | √ | '0' | 虚文档名称 |
| 3 | fdocumentfield | 物理文件字段 | varchar | 50 |  | √ | ' ' | 物理文件字段 |
| 4 | findex | 物料索引 | bpchar | 1 |  | √ | '0' | 物料索引 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 7 | fmetadatajson | 元数据信息json | varchar | 255 |  | √ | ' ' | 元数据信息json |
| 8 | fmatmustinput | 物料是否必填 | varchar | 50 |  | √ | ' ' | 物料是否必填 |
| 9 | fmatpropertyname | 物料字段多语言 | varchar | 50 |  | √ | ' ' | 物料字段多语言 |
| 10 | fmatpropertycode | 物料字段属性编码 | varchar | 50 |  | √ | ' ' | 物料字段属性编码 |
| 11 | fmustinput | 文档是否必填 | varchar | 50 |  | √ | ' ' | 文档是否必填 |
| 12 | ffieldtype | 字段类别 | varchar | 50 |  | √ | ' ' | 字段类别,枚举: ModelField :模型属性 ClassifyField :分类属性 |
| 13 | fmetadatajson_tag | 元数据信息json_详情 | text | 0 |  |  | null | 元数据信息json_详情 |
| 14 | fepropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: NORMAL :一般字段 BOM :BOM字段 |
| 15 | fdocumentindex | 文件索引 | bpchar | 1 |  | √ | '0' | 文件索引 |
| 16 | fpropertycode | 文档字段编码 | varchar | 50 |  | √ | ' ' | 文档字段编码 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fpropertyname | 文档字段多语言 | varchar | 50 |  | √ | ' ' | 文档字段多语言 |
| 19 | fmaterialmodel | 模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 20 | fmaterialclass | 分类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_detail_mapping |  | fentryid |
| 2 | idx_plmdc_detail_mapping_fk |  | fid |

---

## 生成BOM规则配置单据体-子表 t_plmdc_filetype_bomrule

- **表名称：** 生成BOM规则配置单据体-子表
- **表名：** t_plmdc_filetype_bomrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchtype | 物料匹配方式 | varchar | 50 |  | √ | ' ' | 物料匹配方式,枚举: A :手动选择 B :自动生成 |
| 3 | fbomlevel | 层级 | int4 | 32 |  | √ | 0 | 层级 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fruledesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_filetype_bomrule |  | fentryid |
| 2 | idx_plmdc_filetype_bomrule |  | fid |

---

## 文件扩展名单据体-子表 t_plmdc_filetype_entry

- **表名称：** 文件扩展名单据体-子表
- **表名：** t_plmdc_filetype_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fextname | 扩展名 | varchar | 50 |  | √ | ' ' | 扩展名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmdc_filetype_entry |  | fentryid |
| 2 | idx_plmdc_filetype_entry_fk |  | fid |
