# 组合识别器-cvp_cls_info

## 单据体-子表 t_cvp_classifier_config

- **表名称：** 单据体-子表
- **表名：** t_cvp_classifier_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fincludedtemplate | 模版名称 | int8 | 64 |  | √ | 0 | 模板基础资料 cvp_template_base |
| 3 | fmodifydate | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 4 | fkeyoword | 分类关键字 | varchar | 1000 |  |  | ' ' | 分类关键字 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_classifier_config |  | fincludedtemplate |
| 2 | pk_t_cvp_classifier_config |  | fentryid |

---

## 组合识别器-主表 t_cvp_classifier_info

- **表名称：** 组合识别器-主表
- **表名：** t_cvp_classifier_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 组合识别器名称 | varchar | 50 |  |  | ' ' | 组合识别器名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fstatus | 状态 | varchar | 50 |  |  | ' ' | 状态,枚举: A :未发布 B :已发布-有更新 C :可用 D :禁用 E :发布可用 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fbillisperset | 是否预置 | varchar | 50 |  |  | ' ' | 是否预置,枚举: A :是 B :否 |
| 10 | fclassifiermethod | 分类方法 | varchar | 50 |  |  | ' ' | 分类方法,枚举: 1 :关键字 2 :图片 |
| 11 | fenable | 使用状态 | varchar | 50 |  |  | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 组合识别器编码 | varchar | 30 |  |  | ' ' | 组合识别器编码 |
| 13 | fdesc | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 14 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_classifier_info |  | fid |
| 2 | idx_cvp_classifier_info |  | fnumber,fname |

---

## 图片集-附件表 t_cvp_classifier_files

- **表名称：** 图片集-附件表
- **表名：** t_cvp_classifier_files

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__cvp_classifier_files |  | fbasedataid |
| 2 | pk_t_cvp_classifier_files |  | fpkid |

---

## 组合识别器-多语言表 t_cvp_classifier_info_l

- **表名称：** 组合识别器-多语言表
- **表名：** t_cvp_classifier_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 组合识别器名称 | varchar | 50 |  |  | ' ' | 组合识别器名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_classifier_info_l |  | fid |
| 2 | pk_t_cvp_classifier_info_l |  | fpkid |
