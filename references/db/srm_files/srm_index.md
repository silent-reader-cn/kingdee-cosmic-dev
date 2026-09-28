# 评估指标-srm_index

## 评估类型-多选基础资料表 t_pur_index_evatype

- **表名称：** 评估类型-多选基础资料表
- **表名：** t_pur_index_evatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_index_evatype_pkey |  | fpkid |
| 2 | idx_pur_index_evatype_fid |  | fid,fbasedataid |

---

## 指标对象分录-子表 t_pur_indexentry1

- **表名称：** 指标对象分录-子表
- **表名：** t_pur_indexentry1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisgenericrule | 是否通用规则 | bpchar | 1 |  | √ | '1' | 是否通用规则 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcategoryid | 品类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_indexentry1_fid_fseq |  | fid,fseq |
| 2 | pk_pur_indexentry1 |  | fentryid |

---

## 评估组织-多选基础资料表 t_pur_index_org

- **表名称：** 评估组织-多选基础资料表
- **表名：** t_pur_index_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_index_org |  | fpkid |
| 2 | idx_pur_index_org_fid |  | fid,fbasedataid |

---

## 评估品类-多选基础资料表 t_pur_index_category

- **表名称：** 评估品类-多选基础资料表
- **表名：** t_pur_index_category

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_index_category |  | fpkid |
| 2 | idx_pur_index_category_fid |  | fid,fbasedataid |

---

## 评分规则分录（旧）-子表 t_pur_indexentry

- **表名称：** 评分规则分录（旧）-子表
- **表名：** t_pur_indexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaluefrom | 考核值从(大于等于) | numeric | 19 | 6 | √ | 0.000000 | 考核值从(大于等于) |
| 3 | fvalueto | 考核值至(小于) | numeric | 19 | 6 | √ | 0.000000 | 考核值至(小于) |
| 4 | fveto | 一票否决 | bpchar | 1 |  | √ | ' ' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 5 | fitem | 评分项 | varchar | 255 |  | √ | ' ' | 评分项 |
| 6 | fformula | 得分（计算公式） | varchar | 100 |  | √ | ' ' | 得分（计算公式） |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fitemscore | 得分 | numeric | 19 | 6 | √ | 0.000000 | 得分 |
| 10 | faccordance | 符合项值 | varchar | 50 |  | √ | ' ' | 符合项值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_indexentry_pkey |  | fentryid |
| 2 | idx_pur_indexentry_fid_fseq |  | fid,fseq |

---

## 评估指标-主表 t_pur_index

- **表名称：** 评估指标-主表
- **表名：** t_pur_index

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisevatype | 设定评估类型 | bpchar | 1 |  | √ | ' ' | 设定评估类型 |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fformulaid | 计算公式 | int8 | 64 |  | √ | 0 | [计算公式配置 srm_cal_formula](../srm_files/srm_cal_formula.md) |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fapiplugin | 指标对应的API插件类名(全限定名) | varchar | 100 |  | √ | ' ' | 指标对应的API插件类名(全限定名) |
| 8 | fisformula | 计算公式 | bpchar | 1 |  | √ | ' ' | 计算公式 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 11 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :手工评分 9 :自动评分 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | [指标分类 srm_indexclass](../srm_files/srm_indexclass.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fisorg | 设置组织范围 | bpchar | 1 |  | √ | ' ' | 设置组织范围 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fproperty | 指标性质 | bpchar | 1 |  | √ | ' ' | 指标性质,枚举: 1 :定量指标 2 :定性指标 3 :符合项指标 |
| 24 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 25 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 29 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标分类 srm_indexclass](../srm_files/srm_indexclass.md) |
| 30 | fiscategory | 设置品类范围 | bpchar | 1 |  | √ | ' ' | 设置品类范围 |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 33 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fisdeduct | 扣分指标 | bpchar | 1 |  | √ | ' ' | 扣分指标 |
| 35 | fscore | 指标最高分值 | numeric | 19 | 6 | √ | 0.000000 | 指标最高分值 |
| 36 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_index_findexclassid |  | findexclassid |
| 2 | idx_pur_index_fnumber |  | fnumber |
| 3 | idx_t_pur_index_createorg |  | fcreateorgid |
| 4 | idx_t_pur_index_master |  | fmasterid |
| 5 | t_pur_index_pkey |  | fid |

---

## 评分规则-子表 t_pur_indexentry1sub

- **表名称：** 评分规则-子表
- **表名：** t_pur_indexentry1sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvaluefrom | 考核值从(大于等于) | numeric | 19 | 6 | √ | 0 | 考核值从(大于等于) |
| 2 | fvalueto | 考核值至(小于) | numeric | 19 | 6 | √ | 0 | 考核值至(小于) |
| 3 | fveto | 一票否决 | bpchar | 1 |  | √ | ' ' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :本次绩效0分 9 :非否决项 |
| 4 | fitem | 评分项 | varchar | 255 |  | √ | ' ' | 评分项 |
| 5 | fformula | 得分（计算公式） | varchar | 100 |  | √ | ' ' | 得分（计算公式） |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fitemscore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |
| 10 | faccordance | 符合项值 | varchar | 50 |  | √ | ' ' | 符合项值 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_indexentry1sub |  | fdetailid |
| 2 | idx_pur_index1esub_feid_fseq |  | fseq,fentryid |

---

## 评估指标-使用范围位图表 t_pur_index_m

- **表名称：** 评估指标-使用范围位图表
- **表名：** t_pur_index_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_index_m |  | forgid |

---

## 评估指标-多语言表 t_pur_index_l

- **表名称：** 评估指标-多语言表
- **表名：** t_pur_index_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_index_l_fid_flocaleid |  | fid,flocaleid |
| 2 | t_pur_index_l_pkey |  | fpkid |

---

## 评估指标-使用范围表 t_pur_index_u

- **表名称：** 评估指标-使用范围表
- **表名：** t_pur_index_u

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
| 1 | idx_t_pur_index_u_uo |  | fuseorgid |
| 2 | t_pur_index_u_pkey |  | fdataid,fuseorgid |
