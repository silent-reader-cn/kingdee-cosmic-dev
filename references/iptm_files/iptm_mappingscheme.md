# 映射方案[废弃]-iptm_mappingscheme

## 映射方案[废弃]-多语言表 t_iptm_mappingscheme_l

- **表名称：** 映射方案[废弃]-多语言表
- **表名：** t_iptm_mappingscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_mappingscheme_l |  | fpkid |
| 2 | idx_iptm_mappingscheme_lid |  | fid,flocaleid |

---

## 映射方案[废弃]-主表 t_iptm_mappingscheme

- **表名称：** 映射方案[废弃]-主表
- **表名：** t_iptm_mappingscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fimportobj | 引入对象 | varchar | 50 |  | √ | ' ' | 引入对象 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | flastmodified | 是否最近映射 | bpchar | 1 |  | √ | ' ' | 是否最近映射 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_mappingscheme_coil |  | fcreatorid,fimportobj,flastmodified |
| 2 | pk_iptm_mappingscheme |  | fid |
| 3 | idx_iptm_mappingscheme_num |  | fnumber |

---

## 树形单据体-子表 t_iptm_mappingrelation

- **表名称：** 树形单据体-子表
- **表名：** t_iptm_mappingrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftagid | 旗舰字段标识ID | varchar | 50 |  | √ | ' ' | 旗舰字段标识ID |
| 3 | flocal | 页签名 | varchar | 50 |  | √ | ' ' | 页签名 |
| 4 | fcheckkey | 指定关键字段 | bpchar | 1 |  | √ | ' ' | 指定关键字段 |
| 5 | fkdfieldname | 旗舰字段名称 | varchar | 50 |  | √ | ' ' | 旗舰字段名称 |
| 6 | fimpfieldname | 引入字段名称 | varchar | 50 |  | √ | ' ' | 引入字段名称 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | flocalgroup | 页签 | varchar | 50 |  | √ | ' ' | 页签 |
| 11 | fimpfieldcolindex | 引入字段索引 | int4 | 32 |  | √ | 0 | 引入字段索引 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_mappingrelation |  | fentryid |
| 2 | idx_iptm_mappingrelation_id |  | fid |
