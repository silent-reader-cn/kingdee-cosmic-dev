# 综合计算日志-src_bidassess_log

## 综合计算日志-主表 t_src_bidassesslog

- **表名称：** 综合计算日志-主表
- **表名：** t_src_bidassesslog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 综合计算情况 | varchar | 510 |  | √ | ' ' | 综合计算情况 |
| 3 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fcreatetime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 6 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fschemeid | 推荐方案 | int8 | 64 |  | √ | 0 | [推荐方案 src_pattern](../src_files/src_pattern.md) |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | fratio_biz | 商务标占比(%) | numeric | 19 | 2 | √ | 0 | 商务标占比(%) |
| 11 | fratio_tec | 技术标占比(%) | numeric | 19 | 2 | √ | 0 | 技术标占比(%) |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 13 | fcreatorid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 15 | fratio_syn | 综合评标占比(%) | numeric | 19 | 2 | √ | 0 | 综合评标占比(%) |
| 16 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fratio_oth | 商务综合占比(%) | numeric | 19 | 2 | √ | 0 | 商务综合占比(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_bidassesslog |  | fid |
| 2 | idx_src_bidassesslog_pid |  | fprojectid |

---

## 评标结果分录-子表 t_src_bidassesslogentry

- **表名称：** 评标结果分录-子表
- **表名：** t_src_bidassesslogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frank | 排名 | int4 | 32 |  | √ | 0 | 排名 |
| 3 | fothscore | 商务综合得分 | numeric | 19 | 4 | √ | 0 | 商务综合得分 |
| 4 | fpkggroupid | 标段分组 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 5 | fbizamount | 商务价格 | numeric | 19 | 2 | √ | 0 | 商务价格 |
| 6 | fbasetype | 基本类型 | bpchar | 1 |  | √ | ' ' | 基本类型,枚举: 1 :技术标 2 :商务标 3 :商务综合 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsuppliercode | 供应商代码 | varchar | 100 |  | √ | ' ' | 供应商代码 |
| 9 | fresult | 推荐结果 | bpchar | 1 |  | √ | ' ' | 推荐结果,枚举: 1 :中标 2 :备选 3 :未中标 5 :培养 6 :不推荐/门槛未达标 7 :资审/评标不合格 9 :预中标 0 :流标 |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 12 | floctaxamount | 含税金额合计 | numeric | 23 | 10 | √ | 0 | 含税金额合计 |
| 13 | fbizscore | 商务得分 | numeric | 19 | 4 | √ | 0 | 商务得分 |
| 14 | favgvalue | 平均值 | numeric | 19 | 4 | √ | 0 | 平均值 |
| 15 | fbasevalue | 基准值 | numeric | 19 | 6 | √ | 0 | 基准值 |
| 16 | fmaxvalue | 最大值 | numeric | 19 | 4 | √ | 0 | 最大值 |
| 17 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 18 | fsumscore | 总得分 | numeric | 19 | 4 | √ | 0 | 总得分 |
| 19 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 20 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 21 | fminvalue | 最小值 | numeric | 19 | 4 | √ | 0 | 最小值 |
| 22 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 23 | ftecscore | 技术得分 | numeric | 19 | 4 | √ | 0 | 技术得分 |
| 24 | flocamount | 未税金额合计 | numeric | 23 | 10 | √ | 0 | 未税金额合计 |
| 25 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fmaterialname | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_bidassesslogentry_fid |  | fid |
| 2 | pk_src_bidassesslogentry |  | fentryid |
