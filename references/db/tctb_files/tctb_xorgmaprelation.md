# 税务组织映射关系变更单-tctb_xorgmaprelation

## 税务组织映射关系变更单-多语言表 t_tctb_xorgmaprelation_l

- **表名称：** 税务组织映射关系变更单-多语言表
- **表名：** t_tctb_xorgmaprelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
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
| 1 | idx_tctb_xorgmaprelation_l_0 |  | fentryid,flocaleid |
| 2 | pk_tctb_xorgmaprelation_l |  | fpkid |

---

## 映射关系-子表 t_tctb_xorgmapbusobject

- **表名称：** 映射关系-子表
- **表名：** t_tctb_xorgmapbusobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxcategory | 适用税种编码 | varchar | 400 |  | √ | ' ' | 适用税种编码 |
| 2 | fentrysrcid | 源分录行ID | int8 | 64 |  | √ | 0 | 源分录行ID |
| 3 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 4 | fbusinessid | 业务对象id | varchar | 80 |  | √ | ' ' | 业务对象id |
| 5 | fbusinessnumber | 业务对象编码 | varchar | 80 |  | √ | ' ' | 业务对象编码 |
| 6 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 7 | fbusinessname | 业务对象名称 | varchar | 150 |  | √ | ' ' | 业务对象名称 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 12 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_xorgmapbus_fk |  | fentryid |
| 2 | pk_tctb_xorgmapbusobject |  | fdetailid |

---

## 税务组织映射关系变更单-主表 t_tctb_xorgmaprelation

- **表名称：** 税务组织映射关系变更单-主表
- **表名：** t_tctb_xorgmaprelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 映射方案 | int8 | 64 |  | √ | 0 | 税务组织映射方案 tctb_orgmapentity |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsourcebillentity | 源单实体 | varchar | 50 |  | √ | ' ' | 源单实体 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 7 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 11 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 12 | fsourcebillno | 税务组织映射编码 | varchar | 120 |  | √ | ' ' | 税务组织映射编码 |
| 13 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 14 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcebillstatus | 映射关系单据状态 | varchar | 50 |  | √ | ' ' | 映射关系单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 19 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 20 | fvalidstatus | 生效状态 | varchar | 50 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 21 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 22 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_xorgmaprelation |  | fentryid |
| 2 | idx_tctb_xorgmr_sourceid |  | fsourcebillid |
