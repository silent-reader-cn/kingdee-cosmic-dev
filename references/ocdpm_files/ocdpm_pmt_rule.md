# 促销匹配规则-ocdpm_pmt_rule

## 促销匹配入参字段映射-子表 t_ocdpm_pr_fieldmap

- **表名称：** 促销匹配入参字段映射-子表
- **表名：** t_ocdpm_pr_fieldmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finparam | 入参字段 | int8 | 64 |  | √ | 0 | 促销匹配服务入参 ocdpm_pparamdetail |
| 3 | fquerycolname | 适用单据字段 | varchar | 80 |  | √ | ' ' | 适用单据字段,枚举: |
| 4 | fbillcolname | 字段查询标识 | varchar | 80 |  | √ | ' ' | 字段查询标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsourceentity | 所属分录标识 | varchar | 80 |  | √ | ' ' | 所属分录标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_pr_fieldmap |  | fentryid |
| 2 | idx_ocdpm_pr_fieldmap_fid |  | fid |

---

## 促销匹配规则-使用范围表 t_ocdpm_pmtruleset_u

- **表名称：** 促销匹配规则-使用范围表
- **表名：** t_ocdpm_pmtruleset_u

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
| 1 | idx_t_ocdpm_pmtruleset_u_uo |  | fuseorgid |
| 2 | pk_t_ocdpm_pmtruleset_u |  | fdataid,fuseorgid |

---

## 促销匹配规则-主表 t_ocdpm_pmtruleset

- **表名称：** 促销匹配规则-主表
- **表名：** t_ocdpm_pmtruleset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffiltercontent_tag | 匹配规则自定义条件(废弃)_详情 | text | 0 |  |  | null | 匹配规则自定义条件(废弃)_详情 |
| 8 | ffilterscheme | 匹配规则自定义条件 | text | 0 |  |  | null | 匹配规则自定义条件 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpromlink | 促销环节 | bpchar | 1 |  | √ | ' ' | 促销环节,枚举: B :供应链 A :全渠道（渠道间交易） C :全渠道（渠道向企业交易） |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fentryfilter | 不参与促销匹配分录过滤 | text | 0 |  |  | null | 不参与促销匹配分录过滤 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ffiltercontent | 匹配规则自定义条件(废弃) | varchar | 255 |  | √ | ' ' | 匹配规则自定义条件(废弃) |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fbillentity | 适用单据 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocdpm_pmtruleset_master |  | fmasterid |
| 2 | idx_ocdpm_pmtruleset_num |  | fnumber |
| 3 | idx_t_ocdpm_pmtruleset_createorg |  | fcreateorgid |
| 4 | pk_ocdpm_pmtruleset |  | fid |

---

## 促销匹配规则-多语言表 t_ocdpm_pmtruleset_l

- **表名称：** 促销匹配规则-多语言表
- **表名：** t_ocdpm_pmtruleset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_pmtruleset_l |  | fpkid |
| 2 | idx_ocdpm_pmtrulesetl_flid |  | fid,flocaleid |
