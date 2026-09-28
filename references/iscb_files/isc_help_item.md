# 集成云帮助信息-isc_help_item

## 集成云帮助信息-多语言表 t_iscb_help_item_l

- **表名称：** 集成云帮助信息-多语言表
- **表名：** t_iscb_help_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 主题 | varchar | 500 |  | √ | ' ' | 主题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_help_item_l_0 |  | fid,flocaleid |
| 2 | pk_t_iscb_help_item_l |  | fpkid |

---

## 集成云帮助信息-主表 t_iscb_help_item

- **表名称：** 集成云帮助信息-主表
- **表名：** t_iscb_help_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcategory_id | 分类 | int8 | 64 |  | √ | 0 | 集成云帮助分类 isc_help_category |
| 5 | fhelp_content | 帮助内容 | varchar | 255 |  | √ | ' ' | 帮助内容 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fhelp_text | 帮助内容（废弃） | varchar | 2000 |  | √ | ' ' | 帮助内容（废弃） |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftarget_scens | 适用场景 | varchar | 50 |  | √ | ' ' | 适用场景,枚举: ALL :所有脚本场景 VC :值转换规则 QSP :查询服务_参数转换 QSR :查询服务_结果转换 LSP :加载服务_参数转换 LSR :加载服务_结果转换 SFT :服务流程_普通转移 SFE :服务流程_错误转移 SFS :服务流程_脚本节点 SFV :服务流程_过滤条件表达式 DCQ :数据集成_查询脚本 DCT :数据集成_转换脚本 DTL :数据集成_目标数据处理脚本 DCR :数据集成_来源数据处理脚本 FV :数据集成_过滤条件赋值 PV :启动方案_参数赋值 MQPR :消息发布前处理脚本 MQSR :消息预处理脚本 MF :消息发布_格式化脚本 MP :消息订阅_解析脚本 SA :自定义API ATS :API定时调度 AMS :API消息调用 AES :API事件调用 MICROSERVICES :微服务 SQL_EXE :SQL执行工具 DMA :数据集成_聚合运算 DMV :数据集成_直接赋值 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fauthor | 作者 | varchar | 50 |  | √ | ' ' | 作者 |
| 14 | fhelp_content_tag | 帮助内容_详情 | text | 0 |  |  | null | 帮助内容_详情 |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_help_item_0 |  | fnumber |
| 2 | pk_t_iscb_help_item |  | fid |
