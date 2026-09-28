# 提取记录-ai_trace

## 提取记录-多语言表 t_ai_trace_l

- **表名称：** 提取记录-多语言表
- **表名：** t_ai_trace_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilename | 文件名称 | varchar | 150 |  | √ | '' | 文件名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | '' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_trace_l |  | fpkid |
| 2 | idx_ai_trace_ffilename |  | ffilename |
| 3 | idx_ai_trace_fid |  | fid,flocaleid |

---

## 提取记录-主表 t_ai_trace

- **表名称：** 提取记录-主表
- **表名：** t_ai_trace

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextractstatus | 提取状态 | varchar | 50 |  | √ | '' | 提取状态,枚举: extracting :提取中 extraction failed :提取失败 extraction successful :提取成功 |
| 3 | fexforminfoid | 表格解析id | int8 | 64 |  | √ | 0 | 表格解析id |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffilesource | 文件来源 | varchar | 20 |  | √ | '' | 文件来源,枚举: PC :PC Model :Model |
| 7 | factive | 数据状态 | bpchar | 1 |  | √ | '1' | 数据状态,枚举: 0 :禁用 1 :启用 |
| 8 | fprogress | 处理进度 | varchar | 50 |  | √ | '' | 处理进度,枚举: table recog proceed :表格提取中 KIE extracting :关键信息提取中 KIE end :关键信息提取完成 table recog failed :表格提取失败 KIE failed :关键信息提取失败 |
| 9 | ferrmessage | 错误信息 | varchar | 1024 |  | √ | '' | 错误信息 |
| 10 | ffileurl | 文件位置 | varchar | 1024 |  | √ | '' | 文件位置 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | foribillno | 原单据编号 | varchar | 50 |  | √ | '' | 原单据编号 |
| 13 | fexmodelinfoid | 模型解析id | int8 | 64 |  | √ | 0 | 模型解析id |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ffilename | 文件名称 | varchar | 150 |  | √ | '' | 文件名称 |
| 16 | fpages | 总页数 | int2 | 16 |  | √ | 0 | 总页数 |
| 17 | ffileid | 文件id | varchar | 50 |  | √ | '' | 文件id |
| 18 | fnumber | 编号 | varchar | 50 |  | √ | '' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_trace_fnumber |  | fnumber |
| 2 | pk_t_ai_trace |  | fid |
