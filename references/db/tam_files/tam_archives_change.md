# 税务档案变更记录-tam_archives_change

## 变更明细-子表 t_tam_change_detail

- **表名称：** 变更明细-子表
- **表名：** t_tam_change_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faftervalue | 变更后 | varchar | 300 |  | √ | ' ' | 变更后 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fchangetype | 变更项目 | varchar | 50 |  | √ | ' ' | 变更项目 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbeforevalue | 变更前 | varchar | 300 |  | √ | ' ' | 变更前 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tam_change_detail |  | fentryid |
| 2 | idx_tam_change_detail_fk |  | fid |

---

## 税务档案变更记录-多语言表 t_tam_archives_change_l

- **表名称：** 税务档案变更记录-多语言表
- **表名：** t_tam_archives_change_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tam_archives_change_l_0 |  | fid,flocaleid |
| 2 | pk_tam_archives_change_l |  | fpkid |

---

## 税务档案变更记录-主表 t_tam_archives_change

- **表名称：** 税务档案变更记录-主表
- **表名：** t_tam_archives_change

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | farchivesid | 税务档案主键 | varchar | 100 |  | √ | ' ' | 税务档案主键 |
| 4 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tam_archives_change |  | fid |
| 2 | idx_tam_archives_change |  | farchivesid |
