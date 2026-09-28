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
| 6 | fschemeid | 评标方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 7 | fbilldate | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 8 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 9 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 10 | fisaptitude | 是否资质审查 | bpchar | 1 |  | √ | '0' | 是否资质审查 |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fscoretype | 评标方式 | bpchar | 1 |  | √ | ' ' | 评标方式,枚举: 1 :线上评标 2 :线下评标 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 15 | fbillno | 任务单号 | varchar | 30 |  | √ | ' ' | 任务单号 |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fisaptitude2 | 是否资质后审 | bpchar | 1 |  | √ | '0' | 是否资质后审 |
| 18 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 19 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 21 | fsumscore | 评估得分 | numeric | 23 | 10 | √ | 0 | 评估得分 |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 24 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | ffinishdate | 评分完成时间 | timestamp | 0 |  |  | null | 评分完成时间 |
| 26 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 27 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 28 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 29 | fminvalue | 合格最低分 | numeric | 23 | 10 | √ | 0 | 合格最低分 |
| 30 | fbillindexscore | 指标占比(%) | numeric | 23 | 10 | √ | 0 | 指标占比(%) |
| 31 | finputscore | 手工录入得分 | numeric | 23 | 10 | √ | 0 | 手工录入得分 |
| 32 | fbizstatus2 | fbizstatus2 | bpchar | 1 |  | √ | ' ' |  |
| 33 | fisvalid | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格 |
| 34 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_score_packageid |  | fpackageid |
| 2 | idx_src_score_fbillno |  | fbillno |
| 3 | idx_src_score_supid |  | fsupplierid |
| 4 | idx_src_score_projectid |  | fprojectid |
| 5 | pk_src_score |  | fid |
