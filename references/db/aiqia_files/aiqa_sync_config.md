# 向量同步配置-aiqa_sync_config

## 向量同步配置-主表 t_aiqa_rag_sync_config

- **表名称：** 向量同步配置-主表
- **表名：** t_aiqa_rag_sync_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frank | 重排序算法服务实例 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | finstance | embbeding服务实例 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpwd | 密码 | varchar | 50 |  | √ | ' ' | 密码 |
| 8 | fip | IP | varchar | 50 |  | √ | ' ' | IP |
| 9 | fbrandnamemodelrag | 品牌名称型号 | int8 | 64 |  | √ | 0 | [知识库 gai_repo_info](../gai_files/gai_repo_info.md) |
| 10 | fbrandnamerag | 品牌名称 | int8 | 64 |  | √ | 0 | [知识库 gai_repo_info](../gai_files/gai_repo_info.md) |
| 11 | fserviceaddress | 服务地址 | varchar | 200 |  | √ | ' ' | 服务地址 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcollection | collection | varchar | 50 |  | √ | ' ' | collection |
| 14 | fusername | 用户名 | varchar | 50 |  | √ | ' ' | 用户名 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftoken | Token | varchar | 200 |  | √ | ' ' | Token |
| 19 | fbrandrag | 品牌 | int8 | 64 |  | √ | 0 | [知识库 gai_repo_info](../gai_files/gai_repo_info.md) |
| 20 | fport | 端口 | varchar | 50 |  | √ | ' ' | 端口 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fscore | 相似度 | varchar | 50 |  | √ | ' ' | 相似度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aiqa_rag_sync_config_m0 |  | fmasterid |
| 2 | pk_aiqa_rag_sync_config |  | fid |

---

## 向量同步配置-多语言表 t_aiqa_rag_sync_config_l

- **表名称：** 向量同步配置-多语言表
- **表名：** t_aiqa_rag_sync_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aiqa_rag_sync_config_l |  | fpkid |
| 2 | idx_aiqa_rag_sync_config_l_0 |  | fid,flocaleid |
