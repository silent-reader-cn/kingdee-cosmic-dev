# 考评记录F7-src_evaluatetaskf7

## 考评记录F7-主表 t_src_evaluatetask

- **表名称：** 考评记录F7-主表
- **表名：** t_src_evaluatetask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 考评设置分录ID | int8 | 64 |  | √ | 0 | 考评设置分录ID |
| 3 | fgradeschemeid | 分级方案 | int8 | 64 |  | √ | 0 | 考评分级方案 src_expertgrade |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fbasetype | 基本类型 | bpchar | 1 |  | √ | '1' | 基本类型,枚举: 8 :专家考评类 |
| 6 | fbizstatus | 评分状态 | bpchar | 1 |  | √ | ' ' | 评分状态,枚举: A :未启动 B :待评分 C :部分评分 D :已评分 E :已废标 |
| 7 | fschemeid | 评分方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 8 | fbilldate | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 9 | fsuppliercode | 专家代码 | varchar | 50 |  | √ | ' ' | 专家代码 |
| 10 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 11 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :线上评标 2 :线下评标 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 16 | fbillno | 任务单号 | varchar | 30 |  | √ | ' ' | 任务单号 |
| 17 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 18 | fisaptitude2 | fisaptitude2 | bpchar | 1 |  | √ | '0' |  |
| 19 | fprojectid | 考评单号 | int8 | 64 |  | √ | 0 | 专家考评F7 src_evaluatef7 |
| 20 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 21 | fgradeid | 考评等级 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | fsumscore | 评估得分 | numeric | 23 | 10 | √ | 0 | 评估得分 |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 26 | fexperttype | 专家类别 | varchar | 30 |  | √ | ' ' | 专家类别,枚举: src_expert :评标专家 |
| 27 | fsupplierid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 28 | ffinishdate | 评分完成时间 | timestamp | 0 |  |  | null | 评分完成时间 |
| 29 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 30 | fminvalue | 合格最低分 | numeric | 23 | 10 | √ | 0 | 合格最低分 |
| 31 | fbillindexscore | 指标占比(%) | numeric | 23 | 10 | √ | 0 | 指标占比(%) |
| 32 | finputscore | 手工录入得分 | numeric | 23 | 10 | √ | 0 | 手工录入得分 |
| 33 | fbizstatus2 | fbizstatus2 | bpchar | 1 |  | √ | ' ' |  |
| 34 | fisvalid | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格 |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluatetask_supid |  | fsupplierid |
| 2 | pk_src_evaluatetask |  | fid |
| 3 | idx_src_evaluatetask_projectid |  | fprojectid |
| 4 | idx_src_evaluatetask_fbillno |  | fbillno |
