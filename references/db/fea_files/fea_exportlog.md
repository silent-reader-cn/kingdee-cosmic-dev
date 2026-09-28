# 导出文件记录-fea_exportlog

## 导出文件记录-多语言表 t_fea_exportlog_l

- **表名称：** 导出文件记录-多语言表
- **表名：** t_fea_exportlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanname | 导出方案名称 | varchar | 100 |  | √ | ' ' | 导出方案名称 |
| 3 | flocaleid | flocaleid | bpchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_exportlog_l |  | fpkid |
| 2 | idx_fea_exportlog_l |  | fid,flocaleid |

---

## 导出文件记录-主表 t_fea_exportlog

- **表名称：** 导出文件记录-主表
- **表名：** t_fea_exportlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuser | 导出人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ffiletype | 文件格式 | varchar | 100 |  | √ | ' ' | 文件格式 |
| 4 | fplanname | fplanname | varchar | 100 |  | √ | ' ' |  |
| 5 | fdatetime | 导出时间 | timestamp | 0 |  |  | null | 导出时间 |
| 6 | fplan | 导出方案 | int8 | 64 |  | √ | 0 | [导出方案 fea_plan](../fea_files/fea_plan.md) |
| 7 | forg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fplannumber | 导出方案编码 | varchar | 30 |  | √ | ' ' | 导出方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_exportlog |  | fid |
| 2 | idx_fea_exportlog |  | fplan,fuser |
