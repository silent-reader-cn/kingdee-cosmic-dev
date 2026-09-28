# 评标任务F7-src_scoretaskf7

## 评标任务F7-主表 t_src_score

- **表名称：** 评标任务F7-主表
- **表名：** t_src_score

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 评标/资审设置分录ID | int8 | 64 |  | √ | 0 | 评标/资审设置分录ID |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fbasetype | 基本类型 | bpchar | 1 |  | √ | '1' | 基本类型,枚举: 1 :技术类 2 :商务类 3 :商务综合类 4 :资质审查类 5 :供应商分析类 6 :综合评标类 7 :资质后审类 |
| 5 | fbizstatus | 评估状态 | bpchar | 1 |  | √ | ' ' | 评估状态,枚举: A :未启动 B :待评分 C :部分评分 D :已评分 E :已废标 |
| 6 | fschemeid | 评标方案 | int8 | 64 |  | √ | 0 | [方案配置 src_scheme](../src_files/src_scheme.md) |
| 7 | fbilldate | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 8 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 9 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 10 | fisaptitude | 是否资质审查 | bpchar | 1 |  | √ | '0' | 是否资质审查 |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fscoretype | 评标方式 | bpchar | 1 |  | √ | ' ' | 评标方式,枚举: 1 :线上评标 2 :线下评标 |
| 13 | faptituderesult | faptituderesult | bpchar | 1 |  | √ | '0' |  |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 16 | fbillno | 任务单号 | varchar | 30 |  | √ | ' ' | 任务单号 |
| 17 | fispuraptitude | fispuraptitude | bpchar | 1 |  | √ | '0' |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fisaptitude2 | 是否资质后审 | bpchar | 1 |  | √ | '0' | 是否资质后审 |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | fagents | fagents | int8 | 64 |  | √ | 0 |  |
| 24 | fsumscore | 评估得分 | numeric | 23 | 10 | √ | 0 | 评估得分 |
| 25 | faptitudenote | faptitudenote | varchar | 255 |  | √ | ' ' |  |
| 26 | fauditdate | 回复时间 | timestamp | 0 |  |  | null | 回复时间 |
| 27 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 29 | ffinishdate | 评分完成时间 | timestamp | 0 |  |  | null | 评分完成时间 |
| 30 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 31 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 32 | fcfmstatus | 回复状态 | bpchar | 1 |  | √ | 'A' | 回复状态,枚举: A :待回复 B :已提交 C :已回复 |
| 33 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 34 | fminvalue | 合格最低分 | numeric | 23 | 10 | √ | 0 | 合格最低分 |
| 35 | fisaptitudereply | fisaptitudereply | bpchar | 1 |  | √ | '0' |  |
| 36 | fbillindexscore | 指标类型权重（%） | numeric | 23 | 10 | √ | 0 | 指标类型权重（%） |
| 37 | finputscore | 手工录入得分 | numeric | 23 | 10 | √ | 0 | 手工录入得分 |
| 38 | fbizstatus2 | fbizstatus2 | bpchar | 1 |  | √ | ' ' |  |
| 39 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 40 | fcfmstatus_sup | fcfmstatus_sup | bpchar | 1 |  | √ | 'A' |  |
| 41 | fcfmstatus_pur | fcfmstatus_pur | bpchar | 1 |  | √ | 'A' |  |
| 42 | fisvalid | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格 |
| 43 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_score_packageid |  | fpackageid |
| 2 | idx_src_score_supid |  | fsupplierid |
| 3 | idx_src_score_fbillno |  | fbillno |
| 4 | idx_src_score_projectid |  | fprojectid |
| 5 | pk_src_score |  | fid |
