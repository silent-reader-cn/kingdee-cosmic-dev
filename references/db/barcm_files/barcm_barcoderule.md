# 条码规则-barcm_barcoderule

## 条码规则-主表 t_barcm_barcoderule

- **表名称：** 条码规则-主表
- **表名：** t_barcm_barcoderule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbarcodetotallength | 条码总长度 | int8 | 64 |  | √ | 0 | 条码总长度 |
| 3 | fbarcodeexample | 条码示例 | varchar | 2000 |  | √ | ' ' | 条码示例 |
| 4 | fterminatedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fruletype | 规则类型 | bpchar | 1 |  | √ | 'A' | 规则类型,枚举: A :主档对照 B :定长解析 C :分段解析 |
| 7 | fallowsametaskdupscan | 允许同一次作业中重复扫描 | bpchar | 1 |  | √ | '1' | 允许同一次作业中重复扫描 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料ID | int8 | 64 |  | √ | 0 | 原资料ID |
| 15 | fbarcodespecsqty | 条码规格数量 | numeric | 23 | 10 | √ | 0 | 条码规格数量 |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 18 | fqtysrcsigncode | 数量来源字段编号 | varchar | 50 |  | √ | ' ' | 数量来源字段编号 |
| 19 | finallowdupscan | 允许重复扫描入库 | bpchar | 1 |  | √ | '1' | 允许重复扫描入库 |
| 20 | fbarcodenumberrule | 条码个数规则 | bpchar | 1 |  | √ | ' ' | 条码个数规则,枚举: A :依规格数量算 B :依最小包装数算 C :一物一码 D :人工指定 |
| 21 | fsrcbcfieldsign | 条码回填字段标识 | varchar | 50 |  | √ | ' ' | 条码回填字段标识 |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | foutallowdupscan | 允许重复扫描出库 | bpchar | 1 |  | √ | '1' | 允许重复扫描出库 |
| 27 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fpermitreuse | 允许容器重复使用 | bpchar | 1 |  | √ | '0' | 允许容器重复使用 |
| 30 | fcreateorg | fcreateorg | int8 | 64 |  | √ | 0 |  |
| 31 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 32 | fenableserial | 启用序列号管理 | bpchar | 1 |  | √ | '0' | 启用序列号管理 |
| 33 | fbizobjectid | 业务对象 | int8 | 64 |  | √ | 0 | 条码业务对象白名单 barcm_bizobjwhitelist |
| 34 | fbarcodetypeid | 条码类型 | int8 | 64 |  | √ | 0 | 条码类型 barcm_barcodetype |
| 35 | fqtysrcsignname | 数量来源字段 | varchar | 255 |  | √ | ' ' | 数量来源字段 |
| 36 | fmulqtysrcsignname | fmulqtysrcsignname | varchar | 255 |  | √ | ' ' |  |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fconstantmark | 固定标识 | varchar | 50 |  | √ | ' ' | 固定标识 |
| 39 | fcontainertypeid | 包装容器类型 | int8 | 64 |  | √ | 0 | 包装容器类型 barcm_containertype_m |
| 40 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 41 | fisbanautonumber | 禁止流水号自动升位 | bpchar | 1 |  | √ | '0' | 禁止流水号自动升位 |
| 42 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fmanageorg | fmanageorg | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_barcoderule_fnumber |  | fnumber |
| 2 | pk_barcm_barcoderule |  | fid |
| 3 | idx_t_barcm_barcoderule_master |  | fmasterid |
| 4 | idx_t_barcm_barcoderule_createorg |  | fcreateorgid |

---

## 适用打印模板-子表 t_barcm_bcrulesuitprint

- **表名称：** 适用打印模板-子表
- **表名：** t_barcm_bcrulesuitprint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprinttemplateid | 打印模板 | int8 | 64 |  | √ | 0 | 维护打印模板（新） bos_manageprinttpl |
| 3 | fdefaultprint | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcrulesuitprint_fk |  | fid |
| 2 | pk_barcm_bcrulesuitprint |  | fentryid |

---

## 规则内容-子表 t_barcm_bcrulecontent

- **表名称：** 规则内容-子表
- **表名：** t_barcm_bcrulecontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fparentmapbasedataid | 父属性项对应基础资料 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | flength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 5 | fbdattributecode | 基础资料属性编号 | varchar | 50 |  | √ | ' ' | 基础资料属性编号 |
| 6 | finitial | 起始值 | int8 | 64 |  | √ | 0 | 起始值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcutend | 截取结束位 | int8 | 64 |  | √ | 0 | 截取结束位 |
| 9 | fserialnumber | 流水号依据 | bpchar | 1 |  | √ | '0' | 流水号依据 |
| 10 | fattributetypeid | 属性类型 | int8 | 64 |  | √ | 0 | 条码属性类型 barcm_barcodeproptype |
| 11 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :条码属性项 B :基础资料属性 C :固定值 E :系统日期 D :流水号 |
| 12 | fpartakecode | 参与编号 | bpchar | 1 |  | √ | '1' | 参与编号 |
| 13 | fcutbegin | 截取起始位 | int8 | 64 |  | √ | 0 | 截取起始位 |
| 14 | fparentattributeid | 父条码属性项 | int8 | 64 |  | √ | 0 | 条码规则属性项 barcm_barcoderuleprop |
| 15 | faddchar | 补位符 | bpchar | 1 |  | √ | ' ' | 补位符,枚举: A : B :0 |
| 16 | fbdattmapbdatacode | 基础资料属性对应的基础资料标识 | varchar | 50 |  | √ | ' ' | 基础资料属性对应的基础资料标识 |
| 17 | fattributecodeid | 属性项编号 | int8 | 64 |  | √ | 0 | 条码规则属性项 barcm_barcoderuleprop |
| 18 | ffixval | 设置值 | varchar | 50 |  | √ | ' ' | 设置值 |
| 19 | fsplitsign | 分隔符 | bpchar | 1 |  | √ | ' ' | 分隔符,枚举: | :| - :- @ :@ # :# $ :$ % :% ^ :^ & :& * :* [ :[ ] :] _ :_ ; :; |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fformatid | 格式 | int8 | 64 |  | √ | 0 | 格式 barcm_barcodeformat |
| 22 | falignment | 对齐方式 | bpchar | 1 |  | √ | ' ' | 对齐方式,枚举: A :左对齐 B :右对齐 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcrulecontent |  | fentryid |
| 2 | idx_barcm_bacrulecontent_fid |  | fid |

---

## 规则内容-多语言表 t_barcm_bcrulecontent_l

- **表名称：** 规则内容-多语言表
- **表名：** t_barcm_bcrulecontent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
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
| 1 | pk_barcm_bcrulecontent_l |  | fpkid |
| 2 | idx_barcm_bcrulecontent_l |  | fentryid,flocaleid |

---

## 规则分配-子表 t_barcm_bcruledispatch

- **表名称：** 规则分配-子表
- **表名：** t_barcm_bcruledispatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialcfgid | 编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fdefaultbarcodesignid | 默认条码打印模板 | int8 | 64 |  | √ | 0 | 维护打印模板（新） bos_manageprinttpl |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdefaultrule | 默认规则 | bpchar | 1 |  | √ | ' ' | 默认规则 |
| 7 | fdispatchbasis | 分配依据 | varchar | 50 |  | √ | ' ' | 分配依据,枚举: bd_material :按物料 bd_materialgroup :按分类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_bcruledispatch |  | fentryid |
| 2 | pk_barcm_bcruledispatch |  | fentryid |

---

## 条码规则-使用范围表 t_barcm_barcoderule_u

- **表名称：** 条码规则-使用范围表
- **表名：** t_barcm_barcoderule_u

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
| 1 | pk_t_barcm_barcoderule_u |  | fdataid,fuseorgid |
| 2 | idx_t_barcm_barcoderule_u_uo |  | fuseorgid |

---

## 条码规则-多语言表 t_barcm_barcoderule_l

- **表名称：** 条码规则-多语言表
- **表名：** t_barcm_barcoderule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fbarcodeexample | 条码示例 | varchar | 2000 |  | √ | ' ' | 条码示例 |
| 4 | fmulqtysrcsignname | fmulqtysrcsignname | varchar | 255 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_barcoderule_l |  | fid,flocaleid |
| 2 | pk_barcm_barcoderule_l |  | fpkid |
