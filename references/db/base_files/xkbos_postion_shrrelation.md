# 岗位s-HR同步映射关系-xkbos_postion_shrrelation

## 岗位s-HR同步映射关系-多语言表 t_xksec_post_shrrelation_l

- **表名称：** 岗位s-HR同步映射关系-多语言表
- **表名：** t_xksec_post_shrrelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fshrpostname | 岗位名称 | varchar | 80 |  | √ | ' ' | 岗位名称 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xksec_post_shrrelation_l |  | fpkid |
| 2 | idx_xksec_post_shrrelation_l_f |  | fid,flocaleid |

---

## 岗位s-HR同步映射关系-主表 t_xksec_post_shrrelation

- **表名称：** 岗位s-HR同步映射关系-主表
- **表名：** t_xksec_post_shrrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshrpostid | 内码 | varchar | 50 |  | √ | ' ' | 内码 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fpostidtext | fpostidtext | varchar | 50 |  | √ | ' ' |  |
| 5 | fshrpostname | 岗位名称 | varchar | 80 |  | √ | ' ' | 岗位名称 |
| 6 | fpostid | 编码 | int8 | 64 |  | √ | 0 | [岗位 bos_position](../base_files/bos_position.md) |
| 7 | fshrpostnumber | 岗位编码 | varchar | 80 |  | √ | ' ' | 岗位编码 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xksec_post_shrrelation_id |  | fshrpostid,fpostid |
| 2 | pk_t_xksec_post_shrrelation |  | fid |
