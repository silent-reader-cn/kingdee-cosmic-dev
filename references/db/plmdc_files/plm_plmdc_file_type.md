# 文件类型-plm_plmdc_file_type

## 文件类型-主表 t_plmdc_file_type

- **表名称：** 文件类型-主表
- **表名：** t_plmdc_file_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcomponentadminrole | 元器件库管理角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fdocbit | 文档分类匹配位数 | varchar | 50 |  | √ | ' ' | 文档分类匹配位数 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fdoccurrbitvalue | 文档分类位数大小 | int4 | 32 |  | √ | 0 | 文档分类位数大小 |
| 15 | fmatbit | 物料分类匹配位数 | varchar | 50 |  | √ | ' ' | 物料分类匹配位数 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | 文件类型名称 | varchar | 50 |  | √ | ' ' | 文件类型名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdocmatchfield | 文档匹配字段 | varchar | 50 |  | √ | ' ' | 文档匹配字段 |
| 21 | fmatcurrbitvalue | 物料分类位数大小 | int4 | 32 |  | √ | 0 | 物料分类位数大小 |
| 22 | fmatmatchfield | 物料匹配字段 | varchar | 50 |  | √ | ' ' | 物料匹配字段 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fdoctype | 文档类别 | varchar | 50 |  | √ | ' ' | 文档类别,枚举: A :普通 B :2D C :3D D :电子 E :电气 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 文件类型编码 | varchar | 30 |  | √ | ' ' | 文件类型编码 |
| 27 | ffileextension | ffileextension | varchar | 50 |  | √ | ' ' |  |
| 28 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

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
| 2 | fdocfieldtype | 文档字段类别 | varchar | 50 |  | √ | ' ' | 文档字段类别,枚举: ModelField :模型属性 ClassifyField :分类属性 |
| 3 | fvirtualname | 虚文档名称 | bpchar | 1 |  | √ | '0' | 虚文档名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 6 | fmetadatajson | 元数据信息json | varchar | 255 |  | √ | ' ' | 元数据信息json |
| 7 | fmatmustinput | 物料是否必填 | varchar | 50 |  | √ | ' ' | 物料是否必填 |
| 8 | fmatpropertycode | 物料字段属性编码 | varchar | 50 |  | √ | ' ' | 物料字段属性编码 |
| 9 | fmustinput | 文档是否必填 | varchar | 50 |  | √ | ' ' | 文档是否必填 |
| 10 | fmodelpropertyname | fmodelpropertyname | varchar | 50 |  | √ | ' ' |  |
| 11 | fmetadatajson_tag | 元数据信息json_详情 | text | 0 |  |  | null | 元数据信息json_详情 |
| 12 | fepropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: NORMAL :一般字段 BOM :BOM字段 |
| 13 | fdocumentindex | 文件索引 | bpchar | 1 |  | √ | '0' | 文件索引 |
| 14 | fpropertycode | 文档字段编码 | varchar | 50 |  | √ | ' ' | 文档字段编码 |
| 15 | fmaterialmodel | 模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 16 | fmaterialclass | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 17 | fdocumentfield | 物理文件字段 | varchar | 50 |  | √ | ' ' | 物理文件字段 |
| 18 | findex | 物料索引 | bpchar | 1 |  | √ | '0' | 物料索引 |
| 19 | fmodelpropertycode | fmodelpropertycode | varchar | 50 |  | √ | ' ' |  |
| 20 | fedocumentfield | 物理文件字段 | int8 | 64 |  | √ | 0 | [EPLAN属性 plm_plmdc_eplan_attr](../plmdc_files/plm_plmdc_eplan_attr.md) |
| 21 | fmatpropertyname | 物料字段多语言 | varchar | 50 |  | √ | ' ' | 物料字段多语言 |
| 22 | fvirtualnameseq | 虚文档名称序号 | int4 | 32 |  | √ | 0 | 虚文档名称序号 |
| 23 | ffieldtype | 物料字段类别 | varchar | 50 |  | √ | ' ' | 物料字段类别,枚举: ModelField :模型属性 ClassifyField :分类属性 |
| 24 | fcadtitle | 标题栏 | bpchar | 1 |  | √ | '0' | 标题栏 |
| 25 | fcadinfo | 明细栏 | bpchar | 1 |  | √ | '0' | 明细栏 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fpropertyname | 文档字段多语言 | varchar | 50 |  | √ | ' ' | 文档字段多语言 |

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

## 文件扩展名-子表 t_plmdc_file_extension

- **表名称：** 文件扩展名-子表
- **表名：** t_plmdc_file_extension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fextensionname | 扩展名 | varchar | 50 |  | √ | ' ' | 扩展名,枚举: PDF :PDF文件 HTML :HTML文件 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_file_extension |  | fentryid |
| 2 | idx_plmdc_file_extension |  | fid |

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

## 生成BOM规则配置单据体-子表 t_plmdc_electric_bomrule

- **表名称：** 生成BOM规则配置单据体-子表
- **表名：** t_plmdc_electric_bomrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatruledesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | flinkedmark | 关联结构标识 | varchar | 50 |  | √ | ' ' | 关联结构标识,枚举: 10002 :=高层代号 10003 :++安装地点 10004 :+位置代号 10006 :&文件类型 10007 :#用户自定义 11013 :<>原理图 |
| 5 | fmatmatchtype | 物料匹配方式 | varchar | 50 |  | √ | ' ' | 物料匹配方式,枚举: A :手动选择 B :自动生成 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_electric_bomrule |  | fentryid |
| 2 | idx_plmdc_electric_bomrule |  | fid |

---

## 生成BOM规则配置单据体-多语言表 t_plmdc_electric_bomrule_l

- **表名称：** 生成BOM规则配置单据体-多语言表
- **表名：** t_plmdc_electric_bomrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmatruledesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
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
| 1 | pk_t_plmdc_electric_bomrule_l |  | fpkid |
| 2 | idx_plmdc_electric_bomrule_l |  | fentryid,flocaleid |

---

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
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

## 生成物料BOM规则单据体-子表 t_plmdc_generate_rule

- **表名称：** 生成物料BOM规则单据体-子表
- **表名：** t_plmdc_generate_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparttype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: Normal :一般件 Lightening :轻化 Hidden :隐藏 NoContains :不在材料明细表 Drawing :工程图 Compress :压缩 InternalSave :虚拟件 Envelope :封套 Suppressed :隐含 |
| 3 | fgeneratebom | 装配图生成EBOM | varchar | 50 |  | √ | ' ' | 装配图生成EBOM,枚举: 1 :生成 0 :不生成 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fuploadfile | 上传图档 | varchar | 50 |  | √ | ' ' | 上传图档,枚举: 1 :自动上传 0 :不上传 |
| 6 | fgeneratematerial | 图档生成物料 | varchar | 50 |  | √ | ' ' | 图档生成物料,枚举: 0 :不生成 1 :生成 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fdefaultclassify | 物料默认分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 9 | fgeneratedoc | 生成图档对象 | varchar | 50 |  | √ | ' ' | 生成图档对象,枚举: 0 :不生成 1 :生成实文档 2 :生成虚文档 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_generate_rule |  | fentryid |
| 2 | idx_t_plmdc_generate_rule |  | fid,fdefaultclassify |

---

## 绑定物料分类-多选基础资料表 t_plmdc_bind_matclassify

- **表名称：** 绑定物料分类-多选基础资料表
- **表名：** t_plmdc_bind_matclassify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_bind_matclassify |  | fentryid |
| 2 | idx_plmdc_bind_matclassify |  | fpkid |

---

## 明细栏数据对应关系单据体-子表 t_plmdc_detail_mapping

- **表名称：** 明细栏数据对应关系单据体-子表
- **表名：** t_plmdc_detail_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvirtualdocumentname | 虚文档名称 | bpchar | 1 |  | √ | '0' | 虚文档名称 |
| 3 | fdocfieldtype | 文档字段类别 | varchar | 50 |  | √ | ' ' | 文档字段类别,枚举: ModelField :模型属性 ClassifyField :分类属性 |
| 4 | fdocumentfield | 物理文件字段 | varchar | 50 |  | √ | ' ' | 物理文件字段 |
| 5 | findex | 物料索引 | bpchar | 1 |  | √ | '0' | 物料索引 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 8 | fmetadatajson | 元数据信息json | varchar | 255 |  | √ | ' ' | 元数据信息json |
| 9 | fmatmustinput | 物料是否必填 | varchar | 50 |  | √ | ' ' | 物料是否必填 |
| 10 | fmatpropertyname | 物料字段多语言 | varchar | 50 |  | √ | ' ' | 物料字段多语言 |
| 11 | fmatpropertycode | 物料字段属性编码 | varchar | 50 |  | √ | ' ' | 物料字段属性编码 |
| 12 | fmustinput | 文档是否必填 | varchar | 50 |  | √ | ' ' | 文档是否必填 |
| 13 | ffieldtype | 物料字段类别 | varchar | 50 |  | √ | ' ' | 物料字段类别,枚举: ModelField :模型属性 ClassifyField :分类属性 |
| 14 | fmetadatajson_tag | 元数据信息json_详情 | text | 0 |  |  | null | 元数据信息json_详情 |
| 15 | fepropertytype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: NORMAL :一般字段 BOM :BOM字段 |
| 16 | fdocumentindex | 文件索引 | bpchar | 1 |  | √ | '0' | 文件索引 |
| 17 | fpropertycode | 文档字段编码 | varchar | 50 |  | √ | ' ' | 文档字段编码 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fpropertyname | 文档字段多语言 | varchar | 50 |  | √ | ' ' | 文档字段多语言 |
| 20 | fmaterialmodel | 模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 21 | fmaterialclass | 分类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |

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
| 3 | fjoinsigning | 参与签字 | bpchar | 1 |  | √ | ' ' | 参与签字 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fextname | 扩展名 | varchar | 50 |  | √ | ' ' | 扩展名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmdc_filetype_entry |  | fentryid |
| 2 | idx_plmdc_filetype_entry_fk |  | fid |
