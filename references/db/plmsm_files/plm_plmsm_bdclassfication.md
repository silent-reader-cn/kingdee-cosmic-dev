# 分类信息基础资料-plm_plmsm_bdclassfication

## 分类信息基础资料-主表 t_plmsm_classfication_bd

- **表名称：** 分类信息基础资料-主表
- **表名：** t_plmsm_classfication_bd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fparentid | 父类 | int8 | 64 |  | √ | 0 | [分类信息基础资料 plm_plmsm_bdclassfication](../plmsm_files/plm_plmsm_bdclassfication.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodelid | 绑定业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 8 | flongnumber | 长编码 | varchar | 2000 |  | √ | ' ' | 长编码 |
| 9 | fisallowapplyextend | 只允许通过物料申请单创建实例是否继承 | bpchar | 1 |  | √ | '1' | 只允许通过物料申请单创建实例是否继承 |
| 10 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 11 | fismodelextend | 业务类型是否继承 | bpchar | 1 |  | √ | '1' | 业务类型是否继承 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ferpclassifyid | ERP分类id | int8 | 64 |  | √ | 0 | ERP分类id |
| 14 | fallowmaterialapply | 只允许通过物料申请单创建实例 | bpchar | 1 |  | √ | '0' | 只允许通过物料申请单创建实例 |
| 15 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 17 | fstandardid | 物料分类标准 | int8 | 64 |  | √ | 0 | 物料分类标准 |
| 18 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | ftype | 是否实例化 | varchar | 10 |  | √ | ' ' | 是否实例化,枚举: 2 :否 1 :是 |
| 22 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fviewseq | 排序字段 | int4 | 32 |  | √ | 0 | 排序字段 |

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

## 重写属性分录-子表 t_plmsm_classfication_bdr

- **表名称：** 重写属性分录-子表
- **表名：** t_plmsm_classfication_bdr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisrequired | 修改后是否必填 | bpchar | 1 |  | √ | '0' | 修改后是否必填 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fshowmaterialapply | 修改后显示在物料申请单上 | bpchar | 1 |  | √ | '0' | 修改后显示在物料申请单上 |
| 5 | fischangeshowprop | 是否修改显示属性 | bpchar | 1 |  | √ | '0' | 是否修改显示属性 |
| 6 | fischangeshowmatapply | 是否修改显示在物料申请单上 | bpchar | 1 |  | √ | '0' | 是否修改显示在物料申请单上 |
| 7 | fischangedefaultval | 是否修改缺省值 | bpchar | 1 |  | √ | '0' | 是否修改缺省值 |
| 8 | fisunique | 修改后是否唯一 | bpchar | 1 |  | √ | '0' | 修改后是否唯一 |
| 9 | fsourcepropertynum | 源属性编码 | varchar | 50 |  | √ | ' ' | 源属性编码 |
| 10 | fdefaultvalue | 修改后缺省值 | varchar | 500 |  | √ | ' ' | 修改后缺省值 |
| 11 | fshowproperty | 修改后是否显示属性 | bpchar | 1 |  | √ | '0' | 修改后是否显示属性 |
| 12 | fischangerequired | 是否修改必填 | bpchar | 1 |  | √ | '0' | 是否修改必填 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fischangeunique | 是否修改唯一 | bpchar | 1 |  | √ | '0' | 是否修改唯一 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_classfication_bdr |  | fentryid |
| 2 | idx_plmsm_cf_bdr_number |  | fsourcepropertynum |

---

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
| 5 | fshowproperty | 是否显示属性 | bpchar | 1 |  | √ | '0' | 是否显示属性 |
| 6 | fdefaultvalue | 缺省值 | varchar | 255 |  | √ | ' ' | 缺省值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fshowmaterialapply | 显示在物料申请单上 | bpchar | 1 |  | √ | '0' | 显示在物料申请单上 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

---

## 单据体-子表 t_plmsm_classfication_mk

- **表名称：** 单据体-子表
- **表名：** t_plmsm_classfication_mk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchkey | 关键字 | varchar | 255 |  | √ | ' ' | 关键字 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmsm_classfication_mk |  | fentryid |
| 2 | idx_plmsm_cf_mk_matchkey |  | fmatchkey |
