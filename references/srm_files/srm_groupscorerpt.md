# 集团评估报告-srm_groupscorerpt

## 评估详情分录-子表 t_srm_groupscorerptentry

- **表名称：** 评估详情分录-子表
- **表名：** t_srm_groupscorerptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscorerptnoid | 评估报告单号 | int8 | 64 |  | √ | 0 | 评估报告单号 srm_scorerptbaseno |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | forgweight | 权重（%） | numeric | 23 | 10 | √ | 0 | 权重（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_groupevarpt_fid |  | fid |
| 2 | pk_srm_groupscorerptentry |  | fentryid |
| 3 | idx_srm_groupevarpt_frptid |  | fscorerptnoid |

---

## 集团评估报告-多语言表 t_srm_groupscorerpt_l

- **表名称：** 集团评估报告-多语言表
- **表名：** t_srm_groupscorerpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 评估名称 | varchar | 100 |  | √ | ' ' | 评估名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_groupscorerpt_l |  | fpkid |
| 2 | idx_srm_gscore_l_idlocale |  | fid,flocaleid |

---

## 集团评估报告-分表 t_srm_groupscorerpt_a

- **表名称：** 集团评估报告-分表
- **表名：** t_srm_groupscorerpt_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 6 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_groupscorerpt_a |  | fid |
| 2 | idx_srm_gscore_a_fcreatetime |  | fcreatetime |

---

## 集团评估报告-主表 t_srm_groupscorerpt

- **表名称：** 集团评估报告-主表
- **表名：** t_srm_groupscorerpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupsumscore | 集团汇总得分 | numeric | 23 | 10 | √ | 0 | 集团汇总得分 |
| 3 | fname | 评估名称 | varchar | 100 |  | √ | ' ' | 评估名称 |
| 4 | fgroupevagradeid | 集团汇总等级 | int8 | 64 |  | √ | 0 | 评估等级 bd_evagrade |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 6 | fmaterialid | 评估物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | forgid | 集团 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fterminatecaltype | 评估组织权重动态调配方案 | bpchar | 1 |  | √ | ' ' | 评估组织权重动态调配方案,枚举: 1 :按权重比例动态调配 2 :平均分配至其他权重 3 :按设置比例直接计算 |
| 9 | fbilldate | 评估日期 | timestamp | 0 |  |  | null | 评估日期 |
| 10 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 11 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 12 | fsupplierid | 评估对象 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 14 | favgcal | 平均计算 | bpchar | 1 |  | √ | ' ' | 平均计算 |
| 15 | fgroupevaplanno | 集团评估计划单号 | varchar | 80 |  | √ | ' ' | 集团评估计划单号 |
| 16 | fplandate | 要求完成日期 | timestamp | 0 |  |  | null | 要求完成日期 |
| 17 | fcategoryid | 评估品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_score_fbilldate |  | fbilldate |
| 2 | idx_srm_score_fbillno |  | fbillno |
| 3 | pk_srm_groupscorerpt |  | fid |
