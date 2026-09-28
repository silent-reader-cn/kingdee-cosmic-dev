# 分类信息基础资料-plm_plmsm_bdclassfication

## 单据体-子表 t_plmsm_classfication_bdp

- **表名称：** 单据体-子表
- **表名：** t_plmsm_classfication_bdp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisrequired | 是否必填 | int8 | 64 |  | √ | 0 | 是否必填 |
| 3 | fisunique | 是否唯一 | int8 | 64 |  | √ | 0 | 是否唯一 |
| 4 | fpropertynum | 属性编码 | varchar | 50 |  | √ | ' ' | 属性编码 |
| 5 | fdefaultvalue | 缺省值 | varchar | 50 |  | √ | ' ' | 缺省值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fshowmaterialapply | 显示在物料申请单上 | bpchar | 1 |  | √ | '0' | 显示在物料申请单上 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_classfication_bdp |  | fentryid |
| 2 | idx_plmsm_cf_bdp_number |  | fpropertynum |

---

## 分类信息基础资料-主表 t_plmsm_classfication_bd

- **表名称：** 分类信息基础资料-主表
- **表名：** t_plmsm_classfication_bd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fparentid | 父类 | int8 | 64 |  | √ | 0 | 分类信息基础资料 plm_plmsm_bdclassfication |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodelid | 绑定模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 8 | flongnumber | 长编码 | varchar | 2000 |  | √ | ' ' | 长编码 |
| 9 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ferpclassifyid | ERP分类id | int8 | 64 |  | √ | 0 | ERP分类id |
| 12 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 14 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | ftype | 是否实例化 | varchar | 10 |  | √ | ' ' | 是否实例化,枚举: 2 :否 1 :是 |
| 18 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_cf_bd_name |  | fname |
| 2 | pk_t_plmsm_classfication_bd |  | fid |

---

## 分类信息基础资料-多语言表 t_plmsm_classfication_bd_l

- **表名称：** 分类信息基础资料-多语言表
- **表名：** t_plmsm_classfication_bd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 2000 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_cf_bd_l_fid |  | fid |
| 2 | pk_t_plmsm_classfication_bd_l |  | fpkid |
