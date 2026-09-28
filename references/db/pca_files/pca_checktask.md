# 检查任务-pca_checktask

## 单据体-子表 t_pca_checktaskentry

- **表名称：** 单据体-子表
- **表名：** t_pca_checktaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 告警级别 | varchar | 50 |  | √ | ' ' | 告警级别,枚举: A :警告 B :错误 |
| 3 | fismodifiable | 允许修改 | bpchar | 1 |  | √ | '1' | 允许修改 |
| 4 | fisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 5 | fispreitem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcheckitemid | 名称 | int8 | 64 |  | √ | 0 | [检查项 pca_checkitem](../pca_files/pca_checkitem.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_checktaskentry |  | fentryid |
| 2 | idx_pca_checktaskentry_fk |  | fid |

---

## 检查任务-主表 t_pca_checktask

- **表名称：** 检查任务-主表
- **表名：** t_pca_checktask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fpurpose | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: A :计算前 B :结账 C :计算后 |
| 9 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 10 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_checktask |  | fid |
| 2 | idx_pca_checktask_num |  | fnumber |
| 3 | idx_pca_checktask_m0 |  | fmasterid |

---

## 检查任务-多语言表 t_pca_checktask_l

- **表名称：** 检查任务-多语言表
- **表名：** t_pca_checktask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_checktask_l |  | fpkid |
| 2 | idx_pca_checktask_l_0 |  | fid,flocaleid |
