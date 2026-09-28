# 知识库配置-gai_repo_config

## 知识库配置-多语言表 t_gai_repo_config_l

- **表名称：** 知识库配置-多语言表
- **表名：** t_gai_repo_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_config_l |  | fpkid |
| 2 | idx_gai_repo_config_l |  | fid |

---

## 知识库配置-主表 t_gai_repo_config

- **表名称：** 知识库配置-主表
- **表名：** t_gai_repo_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freranker | 重排序模型 | varchar | 50 |  |  | null | 重排序模型,枚举: unused :不启用 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | feslog | ES日志 | varchar | 255 |  |  | null | ES日志 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | feslog_tag | ES日志_详情 | text | 0 |  |  | null | ES日志_详情 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  |  | null | 数据状态,枚举: A :新建 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | festesttime | ES测试时间 | timestamp | 0 |  |  | null | ES测试时间 |
| 14 | festestuser | ES测试者 | varchar | 50 |  |  | null | ES测试者 |
| 15 | fnumber | 编码 | varchar | 50 |  |  | null | 编码 |
| 16 | fmilvuslog_tag | 向量库日志_详情 | text | 0 |  |  | null | 向量库日志_详情 |
| 17 | fmilvustesttime | 向量库测试时间 | timestamp | 0 |  |  | null | 向量库测试时间 |
| 18 | fmilvuslog | 向量库日志 | varchar | 255 |  |  | null | 向量库日志 |
| 19 | fmilvustestuser | 向量库测试者 | varchar | 50 |  |  | null | 向量库测试者 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_repo_config |  | fid |
| 2 | idx_gai_repo_config |  | freranker |
