# 排污口基础信息-tcret_pollution_basedata

## 排污口基础信息-主表 t_tcret_pollution_basedat

- **表名称：** 排污口基础信息-主表
- **表名：** t_tcret_pollution_basedat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpwxkznum | 排污许可证编号 | int8 | 64 |  | √ | 0 | [环保税排污许可证 tctb_hjbhs_entry](../tctb_files/tctb_hjbhs_entry.md) |
| 4 | fsthjzgbm | 生态环境主管部门 | varchar | 50 |  | √ | ' ' | 生态环境主管部门 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fweidu | 纬度-度 | int8 | 64 |  | √ | 0 | 纬度-度 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 税源有效期止 | timestamp | 0 |  |  | null | 税源有效期止 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fjingdufen | 经度-分 | int8 | 64 |  | √ | 0 | 经度-分 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fweidufen | 纬度-分 | int8 | 64 |  | √ | 0 | 纬度-分 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fpfksszgswjg | 排放口所属主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 18 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 19 | fscjyszx | 生产经营所在乡 | varchar | 50 |  | √ | ' ' | 生产经营所在乡 |
| 20 | fweidumiao | 纬度-秒 | numeric | 23 | 10 | √ | 0 | 纬度-秒 |
| 21 | fstartdate | 税源有效期起 | timestamp | 0 |  |  | null | 税源有效期起 |
| 22 | fjingdu | 经度-度 | int8 | 64 |  | √ | 0 | 经度-度 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |
| 25 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 26 | fjingdumiao | 经度-秒 | numeric | 23 | 10 | √ | 0 | 经度-秒 |
| 27 | fpfknum | 排放口编号 | varchar | 50 |  | √ | ' ' | 排放口编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_pollution_basedat |  | fid |
| 2 | idx_tcret_pollution_fnumber |  | fnumber |

---

## 排污口基础信息-多语言表 t_tcret_pollution_basedat_l

- **表名称：** 排污口基础信息-多语言表
- **表名：** t_tcret_pollution_basedat_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 排放口或噪声源名称 | varchar | 50 |  | √ | ' ' | 排放口或噪声源名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pollution_basedat_l_0 |  | fid,flocaleid |
| 2 | pk_tcret_pollution_basedat_l |  | fpkid |

---

## 污染物信息-子表 t_tcret_pollution_wrwmc

- **表名称：** 污染物信息-子表
- **表名：** t_tcret_pollution_wrwmc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 4 | fdwse | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fswrwzl | 水污染物种类 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 7 | fbzndz | 标准浓度值 | numeric | 23 | 10 | √ | 0 | 标准浓度值 |
| 8 | fwrwlb | 污染物类别 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 9 | fwrwmc | 污染物名称 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_hbs_bizdefen_tree |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fwrwpfljsff | 污染物排放量计算方法 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_pollution_wrwmc_fk |  | fid |
| 2 | pk_tcret_pollution_wrwmc |  | fentryid |
