# 指标-tctsa_target_info

## 指标-多语言表 t_tctsa_target_info_l

- **表名称：** 指标-多语言表
- **表名：** t_tctsa_target_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tctsa_target_info_l |  | fpkid |
| 2 | idx_tctsa_target_info_l_0 |  | fid,flocaleid |

---

## 标签类型-多选基础资料表 t_tctsa_label_type

- **表名称：** 标签类型-多选基础资料表
- **表名：** t_tctsa_label_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 标签 t_tctb_label_info |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctsa_label_type |  | fid |
| 2 | pk_t_tctsa_label_type |  | fpkid |

---

## 单据体-子表 t_tctsa_target_offset

- **表名称：** 单据体-子表
- **表名：** t_tctsa_target_offset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frange | 偏差范围 | varchar | 100 |  | √ | ' ' | 偏差范围 |
| 3 | fdescribe | 偏差说明 | varchar | 100 |  | √ | ' ' | 偏差说明 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fgrade | 风险等级 | varchar | 30 |  | √ | ' ' | 风险等级,枚举: 1 :高 2 :中 3 :低 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_target_offset_fk |  | fid |
| 2 | pk_t_tctsa_target_offset |  | fentryid |

---

## 指标-主表 t_tctsa_target_info

- **表名称：** 指标-主表
- **表名：** t_tctsa_target_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fjson | 存储公式 | varchar | 510 |  | √ | ' ' | 存储公式 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescribe | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | flablename | 标签名字 | varchar | 100 |  | √ | ' ' | 标签名字 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 15 | fjson_tag | 存储公式_详情 | text | 0 |  |  | null | 存储公式_详情 |
| 16 | ftaxtype | 税种 | varchar | 30 |  | √ | ' ' | 税种,枚举: 1 :增值税 2 :所得税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tctsa_target_info |  | fid |
| 2 | idx_t_tctsa_target_info |  | fnumber |
