# 编报准备（废弃）-fpm_reportpreparation

## 单据体-子表 t_fpm_fpmbillgenrecord

- **表名称：** 单据体-子表
- **表名：** t_fpm_fpmbillgenrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanreportbillids_tag | 计划编制单据id集合_详情 | text | 0 |  |  | null | 计划编制单据id集合_详情 |
| 3 | fexecresultdetail | 执行结果详情 | varchar | 500 |  | √ | ' ' | 执行结果详情 |
| 4 | fopreateuser | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fplanreportbillids | 计划编制单据id集合 | text | 0 |  |  | null | 计划编制单据id集合 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fexectime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 9 | fteviewdetail | 查看执行结果详情 | varchar | 500 |  | √ | ' ' | 查看执行结果详情 |
| 10 | fexecresult | 执行结果 | varchar | 500 |  | √ | ' ' | 执行结果,枚举: succcess :执行成功 failure :执行失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_fpmbillgenrecord |  | fid |
| 2 | pk_t_fpm_fpmbillgenrecord |  | fentryid |

---

## 编报准备（废弃）-主表 t_fpm_reportpreparation

- **表名称：** 编报准备（废弃）-主表
- **表名：** t_fpm_reportpreparation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconvexratetable | fconvexratetable | varchar | 50 |  | √ | ' ' |  |
| 3 | fcontrlevelstopreptime | 受控层级停报时间 | int4 | 32 |  | √ | 0 | 受控层级停报时间 |
| 4 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 5 | fdeclaredays | 申报天数 | int4 | 32 |  | √ | 0 | 申报天数 |
| 6 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 7 | fdeclarestartdate | 每期申报开始日期 | varchar | 50 |  | √ | ' ' | 每期申报开始日期,枚举: PERIOD_START_BEFORE :期间开始日前 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fdefaultstopreptime | 默认停报时间 | int4 | 32 |  | √ | 0 | 默认停报时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fstopreportdays | 停报天数 | int4 | 32 |  | √ | 0 | 停报天数 |
| 13 | forgreporttype | 编报类型 | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 14 | fbodysysmanage | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 15 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fconvexratetableid | 折算汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | freportsublevel | 受控编报主体层级 | varchar | 50 |  | √ | ' ' | 受控编报主体层级,枚举: TWO_AND_BELOW :2级及以下 THREE_AND_BELOW :3级及以下 FOUR_AND_BELOW :4级及以下 FIVE_AND_BELOW :5级及以下 SIX_AND_BELOW :6级及以下 |
| 20 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fstopreportdate | 每期停报日期 | varchar | 50 |  | √ | ' ' | 每期停报日期,枚举: PERIOD_START_BEFORE :期间开始日前 PERIOD_END_BEFORE :期间结束日前 |
| 23 | fisaccreportsubdefine | 是否按编报主体定义停报时间 | bpchar | 1 |  | √ | '0' | 是否按编报主体定义停报时间 |
| 24 | fenable | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 26 | fcombofield | 折算汇率日期 | varchar | 50 |  | √ | ' ' | 折算汇率日期,枚举: REPORT_START_CUR :申报开始日当天 PERIOD_LASTMONTH_END :期间所在月份的上月末 PERIOD_STARTDAY_CUR :期间开始日当日 PERIOD_MONTHFIRST_FIRST :期间所在月份的月初第一天 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_reportpreparation |  | fid |
| 2 | idx_fpm_reportpreparation |  | fnumber |

---

## 编报准备（废弃）-多语言表 t_fpm_reportpreparation_l

- **表名称：** 编报准备（废弃）-多语言表
- **表名：** t_fpm_reportpreparation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_reportpreparation_l |  | fid |
| 2 | pk_t_fpm_reportpreparation_l |  | fpkid |
