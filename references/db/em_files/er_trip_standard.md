# 全球住宿补助标准-er_trip_standard

## 报销级别-多选基础资料表 t_er_select_reimburseleve

- **表名称：** 报销级别-多选基础资料表
- **表名：** t_er_select_reimburseleve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_select_reimburseleve |  | fid |
| 2 | pk_t_er_reimburseleve |  | fpkid |

---

## 全球住宿补助标准-多语言表 t_er_trip_standard_l

- **表名称：** 全球住宿补助标准-多语言表
- **表名：** t_er_trip_standard_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_trip_standard_l_id |  | fpkid |
| 2 | idx_er_trip_standard_l |  | fid |

---

## 全球住宿补助标准-使用范围表 t_er_trip_standard_u

- **表名称：** 全球住宿补助标准-使用范围表
- **表名：** t_er_trip_standard_u

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
| 1 | pk_t_er_trip_standard_u |  | fdataid,fuseorgid |
| 2 | idx_t_er_trip_standard_u_uo |  | fuseorgid |

---

## 阶梯标准-子表 t_er_step_standard

- **表名称：** 阶梯标准-子表
- **表名：** t_er_step_standard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartday | 区间开始天数 | numeric | 23 | 10 | √ | 0 | 区间开始天数 |
| 3 | fstartmileage | 区间开始里程 | numeric | 23 | 10 | √ | 0 | 区间开始里程 |
| 4 | fendday | 区间结束天数 | numeric | 23 | 10 | √ | 0 | 区间结束天数 |
| 5 | fstepstandardamount | 标准 | numeric | 23 | 10 | √ | 0 | 标准 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentrykey | 关键字段 | varchar | 50 |  | √ | ' ' | 关键字段 |
| 8 | fentryremark | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fendmileage | 区间结束里程 | numeric | 23 | 10 | √ | 0 | 区间结束里程 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_step_standard |  | fid |
| 2 | pk_er_step_standard |  | fentryid |

---

## 全球住宿补助标准-主表 t_er_trip_standard

- **表名称：** 全球住宿补助标准-主表
- **表名：** t_er_trip_standard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpeakseasonamount | 旺季标准 | numeric | 23 | 10 | √ | 0 | 旺季标准 |
| 3 | fstardardtype | 业务事项 | int8 | 64 |  | √ | 0 | [业务事项 er_standard_type](../em_files/er_standard_type.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmileagelimit | 里程限额 | numeric | 23 | 10 | √ | 0 | 里程限额 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftriparea | 出差地域 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | ftripexpenseitem | 差旅项目 | int8 | 64 |  | √ | 0 | [差旅项目 er_tripexpenseitem](../em_files/er_tripexpenseitem.md) |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 19 | flimitcontrol | 限额控制 | bpchar | 1 |  | √ | '0' | 限额控制 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | factualreimtrip | 实报实销 | bpchar | 1 |  | √ | '0' | 实报实销 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fctlperiod | 控制周期 | varchar | 25 |  | √ | ' ' | 控制周期,枚举: month :月 season :季 halfyear :半年 year :年 |
| 25 | fcalcexpr | 计算方式 | varchar | 50 |  | √ | ' ' | 计算方式,枚举: 1 :按天数计算 2 :按里程计算 3 :按固定金额 |
| 26 | fstandardamount | 标准 | numeric | 23 | 10 | √ | 0 | 标准 |
| 27 | fisladdersubsidy | 阶梯补贴 | bpchar | 1 |  | √ | '0' | 阶梯补贴 |
| 28 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 31 | fdimension | 业务维度 | varchar | 2000 |  | √ | ' ' | 业务维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_trip_standard_master |  | fmasterid |
| 2 | pk_t_er_trip_standard_id |  | fid |
| 3 | idx_er_trip_standard_number |  | fnumber |
| 4 | idx_t_er_trip_standard_createorg |  | fcreateorgid |

---

## 出差类型-多选基础资料表 t_er_select_triptype

- **表名称：** 出差类型-多选基础资料表
- **表名：** t_er_select_triptype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [出差类型 er_triptype](../em_files/er_triptype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_select_triptype |  | fpkid |
| 2 | idx_er_select_triptype |  | fid |

---

## 阶梯标准-多语言表 t_er_step_standard_l

- **表名称：** 阶梯标准-多语言表
- **表名：** t_er_step_standard_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryremark | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_step_standard_l |  | fpkid |
| 2 | idx_er_step_standard_l |  | fentryid |

---

## 特殊人员-多选基础资料表 t_er_includeperson

- **表名称：** 特殊人员-多选基础资料表
- **表名：** t_er_includeperson

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_includeperson |  | fpkid |
| 2 | idx_er_includeperson |  | fid |
