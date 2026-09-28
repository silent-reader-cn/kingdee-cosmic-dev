# 算法服务-aicc_service

## 算法服务-主表 t_aicc_service

- **表名称：** 算法服务-主表
- **表名：** t_aicc_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 服务名称 | varchar | 200 |  | √ | ' ' | 服务名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | frequestsample | 请求参数示例 | varchar | 255 |  | √ | ' ' | 请求参数示例 |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 算法服务—类型 aicc_servicetype |
| 6 | fresponsesample_tag | 返回结果参数示例_详情 | text | 0 |  |  | ' ' | 返回结果参数示例_详情 |
| 7 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: |
| 8 | fcreatetime | 上架时间 | timestamp | 0 |  |  | null | 上架时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fresponsesample | 返回结果参数示例 | varchar | 255 |  | √ | ' ' | 返回结果参数示例 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 服务编码 | varchar | 30 |  | √ | ' ' | 服务编码 |
| 16 | frequestsample_tag | 请求参数示例_详情 | text | 0 |  |  | ' ' | 请求参数示例_详情 |
| 17 | fdesc | 算法服务说明 | varchar | 2000 |  |  | null | 算法服务说明 |
| 18 | fllmtype | 基础大模型 | int8 | 64 |  | √ | 0 | 基础大模型 aicc_llm |
| 19 | fsupportstream | 是否支持流式 | bpchar | 1 |  | √ | '0' | 是否支持流式 |
| 20 | fversion | 服务版本号 | varchar | 50 |  | √ | ' ' | 服务版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_service_fnumber |  | fnumber |
| 2 | pk_t_aicc_service |  | fid |

---

## 算法服务-多语言表 t_aicc_service_l

- **表名称：** 算法服务-多语言表
- **表名：** t_aicc_service_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 服务名称 | varchar | 50 |  | √ | ' ' | 服务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aicc_service_l |  | fpkid |
| 2 | idx_aicc_service_l_fid |  | fid |
