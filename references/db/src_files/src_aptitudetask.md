# 资审协同查询-src_aptitudetask

## 供应商回复附件-附件表 t_src_aptitudereply_fj

- **表名称：** 供应商回复附件-附件表
- **表名：** t_src_aptitudereply_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_aptitudereply_fj_bid |  | fbasedataid |
| 2 | pk_src_aptitudereply_fj |  | fpkid |
| 3 | idx_src_aptitudereply_fj_fid |  | fentryid |

---

## 指标分录-子表 t_src_scoreentry

- **表名称：** 指标分录-子表
- **表名：** t_src_scoreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 3 | faptitudereplyvalue | 供应商回复值 | varchar | 512 |  | √ | ' ' | 供应商回复值 |
| 4 | ffinalscore | 最终得分 | numeric | 19 | 6 | √ | 0 | 最终得分 |
| 5 | findexdimension | 评分维度 | varchar | 255 |  | √ | ' ' | 评分维度 |
| 6 | fmanscore | 评委评分 | numeric | 19 | 6 | √ | 0 | 评委评分 |
| 7 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 8 | fentrystatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :待回复 B :已提交 C :已回复 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | findexid | 指标名称 | int8 | 64 |  | √ | 0 | [评分指标F7 src_indexf7](../src_files/src_indexf7.md) |
| 11 | findexlibid | findexlibid | int8 | 64 |  | √ | 0 |  |
| 12 | fisveto | 一票否决 | bpchar | 1 |  | √ | '0' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 13 | fisthreshold | 是否门槛值 | bpchar | 1 |  | √ | '0' | 是否门槛值 |
| 14 | fweight | 指标权重% | numeric | 19 | 6 | √ | 0 | 指标权重% |
| 15 | fsysscore | 系统评分 | numeric | 19 | 6 | √ | 0 | 系统评分 |
| 16 | fscored | 指标已评分 | bpchar | 1 |  | √ | ' ' | 指标已评分 |
| 17 | faptitudereply | 供应商回复内容 | varchar | 512 |  | √ | ' ' | 供应商回复内容 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_scoreentry_indexid |  | findexid |
| 2 | pk_src_scoreentry |  | fentryid |
| 3 | idx_src_scoreentry_fid |  | fid |

---

## 评委-多选基础资料表 t_src_assessscorer2

- **表名称：** 评委-多选基础资料表
- **表名：** t_src_assessscorer2

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
| 1 | pk_src_assessscorer2 |  | fpkid |
| 2 | idx_src_assessscorer2_fid |  | fid |
| 3 | idx_src_assessscorer2_bid |  | fbasedataid |

---

## 供应商资审文件-附件表 t_src_supaptattach

- **表名称：** 供应商资审文件-附件表
- **表名：** t_src_supaptattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supaptattach_bid |  | fbasedataid |
| 2 | pk_src_supaptattach |  | fpkid |

---

## 采购方资审文件-附件表 t_src_puraptattach

- **表名称：** 采购方资审文件-附件表
- **表名：** t_src_puraptattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_puraptattach_fbid |  | fbasedataid |
| 2 | pk_src_puraptattach |  | fpkid |

---

## 资审协同查询-主表 t_src_score

- **表名称：** 资审协同查询-主表
- **表名：** t_src_score

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | 评标/资审设置分录ID | int8 | 64 |  | √ | 0 | 评标/资审设置分录ID |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbasetype | 基本类型 | bpchar | 1 |  | √ | '1' | 基本类型,枚举: 1 :技术类 2 :商务类 3 :商务综合类 4 :资质审查类 5 :供应商分析类 6 :综合评标类 7 :资质后审类 |
| 5 | fbizstatus | 评分状态 | bpchar | 1 |  | √ | ' ' | 评分状态,枚举: A :未启动 B :待评分 C :部分评分 D :已评分 E :已作废 |
| 6 | fschemeid | 资审方案 | int8 | 64 |  | √ | 0 | [方案配置 src_scheme](../src_files/src_scheme.md) |
| 7 | fbilldate | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 8 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 9 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 10 | fisaptitude | 是否资质审查 | bpchar | 1 |  | √ | '0' | 是否资质审查 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fscoretype | 评标方式 | bpchar | 1 |  | √ | ' ' | 评标方式,枚举: 1 :线上评标 2 :线下评标 |
| 13 | faptituderesult | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 14 | fcreatorid | 项目创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fispuraptitude | 是否代理资审回复 | bpchar | 1 |  | √ | '0' | 是否代理资审回复 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fisaptitude2 | 是否资质后审 | bpchar | 1 |  | √ | '0' | 是否资质后审 |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fagents | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fsumscore | 评估得分 | numeric | 23 | 10 | √ | 0 | 评估得分 |
| 25 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 29 | ffinishdate | 评分完成时间 | timestamp | 0 |  |  | null | 评分完成时间 |
| 30 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 31 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 32 | fcfmstatus | 回复状态 | bpchar | 1 |  | √ | 'A' | 回复状态,枚举: A :待回复 B :已提交 C :已回复 |
| 33 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 34 | fminvalue | 合格最低分 | numeric | 23 | 10 | √ | 0 | 合格最低分 |
| 35 | fisaptitudereply | fisaptitudereply | bpchar | 1 |  | √ | '0' |  |
| 36 | fbillindexscore | 指标占比(%) | numeric | 23 | 10 | √ | 0 | 指标占比(%) |
| 37 | finputscore | 手工录入评分 | numeric | 23 | 10 | √ | 0 | 手工录入评分 |
| 38 | fbizstatus2 | 评标状态(历史) | bpchar | 1 |  | √ | ' ' | 评标状态(历史),枚举: A :未启动 B :待评分 C :部分评分 D :已评分 E :已废标 |
| 39 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 40 | fcfmstatus_sup | 供应商回复状态 | bpchar | 1 |  | √ | 'A' | 供应商回复状态,枚举: A :待回复 B :已提交 C :已回复 |
| 41 | fcfmstatus_pur | 采购方回复状态 | bpchar | 1 |  | √ | 'A' | 采购方回复状态,枚举: A :待回复 B :已提交 C :已回复 |
| 42 | fisvalid | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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

---

## 评委分录-子表 t_src_scoredetail

- **表名称：** 评委分录-子表
- **表名：** t_src_scoredetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fveto | fveto | varchar | 30 |  | √ | ' ' |  |
| 5 | fisoverthreshold | fisoverthreshold | bpchar | 1 |  | √ | '0' |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | findexid | 评标指标ID | int8 | 64 |  | √ | 0 | 评标指标ID |
| 10 | fscorerweight | 评委权重% | numeric | 23 | 10 | √ | 0 | 评委权重% |
| 11 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 12 | fisveto | 一票否决 | varchar | 30 |  | √ | '0' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | finvalid | 评分异常否 | bpchar | 1 |  | √ | '0' | 评分异常否,枚举: 0 :正常 1 :偏差过大 2 :去掉最低分 3 :去掉最高分 |
| 15 | fpackageid | fpackageid | int8 | 64 |  | √ | 0 |  |
| 16 | fscored | 评委已评分 | bpchar | 1 |  | √ | '0' | 评委已评分 |
| 17 | fisautoscore | 系统自动评分 | bpchar | 1 |  | √ | '0' | 系统自动评分 |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | findexscore | findexscore | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 21 | faverage | faverage | numeric | 23 | 10 | √ | 0 |  |
| 22 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 23 | fsuppliername | fsuppliername | varchar | 100 |  | √ | ' ' |  |
| 24 | fisfitted | 符合否 | bpchar | 1 |  | √ | '0' | 符合否 |
| 25 | freason | 退回重评原因 | varchar | 255 |  | √ | ' ' | 退回重评原因 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 28 | fvalue | 评估值 | numeric | 23 | 10 | √ | 0 | 评估值 |
| 29 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 30 | fscorerscore | 评委评分 | numeric | 23 | 10 | √ | 0 | 评委评分 |
| 31 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_scoredetail |  | fdetailid |
| 2 | idx_src_scoredetail_supid |  | fsupplierid |
| 3 | idx_src_scoredetail_parentid |  | fparentid |
| 4 | idx_src_scoredetail_agentid |  | fagentid |
| 5 | idx_src_scoredetail_scorerid |  | fscorerid |
| 6 | idx_src_scoredetail_entryid |  | fentryid |
| 7 | idx_src_scoredetail_pid |  | fprojectid |
