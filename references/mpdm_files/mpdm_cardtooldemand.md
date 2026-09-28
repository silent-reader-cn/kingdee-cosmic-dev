# 工卡工具需求-mpdm_cardtooldemand

## 工卡工具需求-主表 t_mpdm_cardtooldemand

- **表名称：** 工卡工具需求-主表
- **表名：** t_mpdm_cardtooldemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fworkcardid | 工卡编码 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | frange | 历史时长统计范围(封存) | int8 | 64 |  | √ | 0 | 历史时长统计范围(封存) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fisneedtool | 需要工具 | bpchar | 1 |  | √ | '0' | 需要工具 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 22 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 24 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fmaterialunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fhourunit | 时长单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_cardtooldemand_master |  | fmasterid |
| 2 | idx_cardtool_fworkcardid |  | fworkcardid |
| 3 | pk_t_mpdm_cardtooldemand |  | fid |
| 4 | idx_t_mpdm_cardtooldemand_createorg |  | fcreateorgid |

---

## 附件（封存）-附件表 t_mpdm_cardtoolappendix

- **表名称：** 附件（封存）-附件表
- **表名：** t_mpdm_cardtoolappendix

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_cardtoolappendix |  | fpkid |
| 2 | t_mpdm_toolappix_fdetailid_idx |  | fdetailid |

---

## 工具清单-子表 t_mpdm_cardtooldemanentry

- **表名称：** 工具清单-子表
- **表名：** t_mpdm_cardtooldemanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyorg | 供货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fgroupversion | 替代组版本 | varchar | 80 |  | √ | ' ' | 替代组版本 |
| 4 | fentryownertype | 供应方式 | varchar | 50 |  | √ | ' ' | 供应方式,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 5 | fentrybaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | flocation | 默认仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryhistoryusetime | 历史使用时长（小时） | numeric | 23 | 10 | √ | 0 | 历史使用时长（小时） |
| 9 | fentryreplacegroup | 替代组(封存) | varchar | 255 |  | √ | ' ' | 替代组(封存) |
| 10 | fentryrange | 统计范围（封存） | int8 | 64 |  | √ | 0 | 统计范围（封存） |
| 11 | ftoolsubgroup | 替代组 | int8 | 64 |  | √ | 0 | 工具替代组 mpdm_toolsubgroup |
| 12 | ftoollevel | 工具使用级别 | varchar | 5 |  | √ | ' ' | 工具使用级别,枚举: A :必选 B :可选 |
| 13 | fentryunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fwarehouse | 默认仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 15 | fentrybaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 16 | fentryqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 17 | fentrylevel | 优先级（封存） | int8 | 64 |  | √ | 0 | 优先级（封存） |
| 18 | fentrymaterial | 工具件号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 19 | fentrymandatory | 必选（封存） | bpchar | 1 |  | √ | '0' | 必选（封存） |
| 20 | frepgrpentryid | 替代组entryid | int8 | 64 |  | √ | 0 | 替代组entryid |
| 21 | fentryowner | 供应方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fmeanstype | 工具分类(封存) | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_meanstype |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_cardtooldemanentry |  | fentryid |
| 2 | idx_cardtoolentry_fid |  | fid |
| 3 | idx_cardtoolentry_fmatid |  | fentrymaterial |

---

## 检修设备类型-多选基础资料表 t_mpdm_rtoolmrtype

- **表名称：** 检修设备类型-多选基础资料表
- **表名：** t_mpdm_rtoolmrtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_rtoope_fentryid |  | fentryid,fbasedataid |
| 2 | pk_mpdm_rtoolmrtype |  | fpkid |

---

## 附件-附件表 t_mpdm_cardtlappendix

- **表名称：** 附件-附件表
- **表名：** t_mpdm_cardtlappendix

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cardtlappendix_fk |  | fentryid |
| 2 | pk_mpdm_cardtlappendix |  | fpkid |

---

## 工卡工具需求-使用范围表 t_mpdm_cardtooldemand_u

- **表名称：** 工卡工具需求-使用范围表
- **表名：** t_mpdm_cardtooldemand_u

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
| 1 | idx_t_mpdm_cardtooldemand_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_cardtooldemand_u |  | fdataid,fuseorgid |

---

## 工卡工具需求-多语言表 t_mpdm_cardtooldemand_l

- **表名称：** 工卡工具需求-多语言表
- **表名：** t_mpdm_cardtooldemand_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_cardtooldemand_l |  | fpkid |
| 2 | idx_cardtooll_fid |  | fid,flocaleid |

---

## 工卡工具需求-使用范围位图表 t_mpdm_cardtooldemand_m

- **表名称：** 工卡工具需求-使用范围位图表
- **表名：** t_mpdm_cardtooldemand_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_cardtooldemand_m |  | forgid |

---

## 文档信息（封存）-子表 t_mpdm_cardtooldocentry

- **表名称：** 文档信息（封存）-子表
- **表名：** t_mpdm_cardtooldocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentrypagenumber | 页码（封存） | varchar | 255 |  | √ | ' ' | 页码（封存） |
| 2 | fentrysegment | 段（封存） | varchar | 255 |  | √ | ' ' | 段（封存） |
| 3 | fentrydescribe | 描述（封存） | varchar | 255 |  | √ | ' ' | 描述（封存） |
| 4 | fentrymanualtype | 参考手册类型（封存） | int8 | 64 |  | √ | 0 | 文件类型 mpdm_doctype |
| 5 | fentrymanualnumber | 手册编码(封存) | varchar | 255 |  | √ | ' ' | 手册编码(封存) |
| 6 | fentrymanualversion | 手册版本（封存） | varchar | 255 |  | √ | ' ' | 手册版本（封存） |
| 7 | fentrysection | 节（封存） | varchar | 255 |  | √ | ' ' | 节（封存） |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrychapter | 章（封存） | varchar | 255 |  | √ | ' ' | 章（封存） |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cardtooldocentry_fk |  | fentryid |
| 2 | pk_mpdm_cardtooldocentry |  | fdetailid |

---

## 手册信息-子表 t_mpdm_cardtooldoc

- **表名称：** 手册信息-子表
- **表名：** t_mpdm_cardtooldoc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdocdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fdocpagenumber | 手册章节号 | varchar | 50 |  | √ | ' ' | 手册章节号 |
| 4 | fdocmanualversion | 手册版本 | varchar | 50 |  | √ | ' ' | 手册版本 |
| 5 | fdocmanualnum | 手册编码 | varchar | 50 |  | √ | ' ' | 手册编码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdocname | 手册名称 | varchar | 255 |  | √ | ' ' | 手册名称 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_cardtooldoc |  | fentryid |
| 2 | idx_mpdm_cardtooldoc_fk |  | fid |
