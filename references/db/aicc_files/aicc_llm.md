# API出入参样式-aicc_llm

## API出入参样式-主表 t_aicc_llm

- **表名称：** API出入参样式-主表
- **表名：** t_aicc_llm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fknowledgebase | 知识库处理模式 | varchar | 50 |  | √ | ' ' | 知识库处理模式,枚举: |
| 3 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型 |
| 4 | fparamdemo_tag | 完整参数入参示例_详情 | text | 0 |  |  | ' ' | 完整参数入参示例_详情 |
| 5 | fnostreamjson | 非流结果后处理JSON结构 | varchar | 50 |  | √ | ' ' | 非流结果后处理JSON结构 |
| 6 | fparams | 模型基本参数 | varchar | 255 |  | √ | ' ' | 模型基本参数 |
| 7 | fparamdemo | 完整参数入参示例 | varchar | 255 |  | √ | ' ' | 完整参数入参示例 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fmaxinputtoken | 模型输入最大上下文 | int8 | 64 |  | √ | 0 | 模型输入最大上下文 |
| 13 | fcreativity | 创意模式参数 | varchar | 255 |  | √ | ' ' | 创意模式参数 |
| 14 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmark | 说明备注 | varchar | 500 |  | √ | ' ' | 说明备注 |
| 17 | fprecision | 精确模式参数 | varchar | 255 |  | √ | ' ' | 精确模式参数 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fllmfactory | 模型提供厂商 | varchar | 50 |  | √ | ' ' | 模型提供厂商,枚举: |
| 20 | fcapabilitytags | 模型能力 | varchar | 200 |  |  | ' ' | 模型能力,枚举: A :深度思考 B :function_call |
| 21 | ftestparams | 模型测试参数 | varchar | 500 |  | √ | ' ' | 模型测试参数 |
| 22 | fbalance | 平衡模式参数 | varchar | 255 |  | √ | ' ' | 平衡模式参数 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 25 | fstreamjson | 流式结果后处理JSON结构 | varchar | 50 |  | √ | ' ' | 流式结果后处理JSON结构 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aicc_llm |  | fid |
| 2 | idx_aicc_llm_fnumber |  | fnumber |

---

## API出入参样式-多语言表 t_aicc_llm_l

- **表名称：** API出入参样式-多语言表
- **表名：** t_aicc_llm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aicc_llm_l |  | fpkid |
| 2 | idx_aicc_llm_l_fid |  | fid |
