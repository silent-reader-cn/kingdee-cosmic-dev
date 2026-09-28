# 排污口基础信息-tdm_pollution_basedata

## 排污口基础信息-多语言表 t_tdm_pollution_basedata_l

- **表名称：** 排污口基础信息-多语言表
- **表名：** t_tdm_pollution_basedata_l

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
| 1 | pk_tdm_pollution_basedata_l |  | fpkid |
| 2 | idx_tdm_pollution_basedata_l_0 |  | fid,flocaleid |

---

## 排污口基础信息-主表 t_tdm_pollution_basedata

- **表名称：** 排污口基础信息-主表
- **表名：** t_tdm_pollution_basedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpwxkznum | 排污许可证编号 | int8 | 64 |  | √ | 0 | 环保税排污许可证 tctb_hjbhs_entry |
| 3 | fzszm | 征收子目 | varchar | 50 |  | √ | ' ' | 征收子目 |
| 4 | fsthjzgbm | 生态环境主管部门 | varchar | 50 |  | √ | ' ' | 生态环境主管部门 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fweidu | 纬度-度 | int8 | 64 |  | √ | 0 | 纬度-度 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 税源有效期止 | timestamp | 0 |  |  | null | 税源有效期止 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fwrwlb | 污染物类别 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 13 | fjingdufen | 经度-分 | int8 | 64 |  | √ | 0 | 经度-分 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 16 | fweidufen | 纬度-分 | int8 | 64 |  | √ | 0 | 纬度-分 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fqtgtfw | 其他固体废物 | varchar | 50 |  | √ | ' ' | 其他固体废物 |
| 19 | fpfksszgswjg | 排放口所属主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 20 | fwrwname | 污染物名称 | varchar | 50 |  | √ | ' ' | 污染物名称 |
| 21 | fhygcpfwrwmc | 海洋工程排放污染物名称 | varchar | 50 |  | √ | ' ' | 海洋工程排放污染物名称 |
| 22 | fcpwxsdwrwmc | 产排污系数的污染物名称 | varchar | 50 |  | √ | ' ' | 产排污系数的污染物名称 |
| 23 | fscjyszx | 生产经营所在乡 | varchar | 50 |  | √ | ' ' | 生产经营所在乡 |
| 24 | fweidumiao | 纬度-秒 | numeric | 23 | 10 | √ | 0 | 纬度-秒 |
| 25 | fstartdate | 税源有效期起 | timestamp | 0 |  |  | null | 税源有效期起 |
| 26 | fjingdu | 经度-度 | int8 | 64 |  | √ | 0 | 经度-度 |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fswrwzl | 水污染物种类 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 29 | fnumber | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |
| 30 | fwrwmc | 污染物名称 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_hbs_bizdefen_tree |
| 31 | fcycsdwrwmc | 抽样测算的污染物名称 | varchar | 50 |  | √ | ' ' | 抽样测算的污染物名称 |
| 32 | fjingdumiao | 经度-秒 | numeric | 23 | 10 | √ | 0 | 经度-秒 |
| 33 | fwrwpfljsff | 污染物排放量计算方法 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_hbs_bizdef_entry |
| 34 | fpfknum | 排放口编号 | varchar | 50 |  | √ | ' ' | 排放口编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_pollution_basedata |  | forgid,fnumber |
| 2 | pk_tdm_pollution_basedata |  | fid |
