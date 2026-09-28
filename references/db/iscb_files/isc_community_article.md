# 社区帖子-isc_community_article

## 社区帖子-多语言表 t_isc_community_article_l

- **表名称：** 社区帖子-多语言表
- **表名：** t_isc_community_article_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_c_article_l_fid |  | fid |
| 2 | pk_t_isc_community_article_l |  | fpkid |

---

## 社区帖子-主表 t_isc_community_article

- **表名称：** 社区帖子-主表
- **表名：** t_isc_community_article

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 类别 | int8 | 64 |  | √ | 0 | 社区帖子类别 isc_article_category |
| 5 | fcreatetime | 数据同步时间 | timestamp | 0 |  |  | null | 数据同步时间 |
| 6 | fmodifytime | 帖子更新时间 | timestamp | 0 |  |  | null | 帖子更新时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | farticle_updatetime | 帖子更新时间 | timestamp | 0 |  |  | null | 帖子更新时间 |
| 11 | fsync_time | 数据同步时间 | timestamp | 0 |  |  | null | 数据同步时间 |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | furl | 社区链接 | varchar | 150 |  | √ | ' ' | 社区链接 |
| 14 | fnumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_c_article_number |  | fnumber |
| 2 | pk_t_isc_community_article |  | fid |
