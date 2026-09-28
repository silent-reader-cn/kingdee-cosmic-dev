# 图号规则列表-plm_plmdc_drawnorule

## 图号规则列表-主表 t_plmdc_drawnorule

- **表名称：** 图号规则列表-主表
- **表名：** t_plmdc_drawnorule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 规则编码 | varchar | 50 |  | √ | ' ' | 规则编码 |
| 11 | fsplitsign | 默认段间分隔符 | varchar | 50 |  | √ | ' ' | 默认段间分隔符,枚举: - :- @ :@ # :# $ :$ % :% ^ :^ & :& * :* _ :_ . :. |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_drawnorule |  | fid |
| 2 | idx_plmdc_drawnorule |  | fnumber |

---

## 图号规则列表-多语言表 t_plmdc_drawnorule_l

- **表名称：** 图号规则列表-多语言表
- **表名：** t_plmdc_drawnorule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_drawnorule_l |  | fpkid |
| 2 | idx_plmdc_drawnorule_l_0 |  | fid,flocaleid |

---

## 编码分析-子表 t_plmdc_drawnoruleentry

- **表名称：** 编码分析-子表
- **表名：** t_plmdc_drawnoruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 步长 | int8 | 64 |  | √ | 0 | 步长 |
| 3 | faddstyle | 右侧补位 | varchar | 1 |  | √ | '1' | 右侧补位 |
| 4 | flength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 5 | fformat | 格式 | varchar | 50 |  | √ | ' ' | 格式 |
| 6 | finitial | 起始值 | int8 | 64 |  | √ | 0 | 起始值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fattusingmode | 适用模式 | varchar | 50 |  | √ | ' ' | 适用模式,枚举: 1 :整段编码 2 :分区间段编码 3 :完全取值 4 :属性截断 |
| 9 | fissortitem | 流水号依据 | bpchar | 1 |  | √ | '0' | 流水号依据 |
| 10 | fgroupdrawno | 图号分组 | varchar | 50 |  | √ | ' ' | 图号分组 |
| 11 | fsettingvalue | 设置值 | varchar | 50 |  | √ | ' ' | 设置值 |
| 12 | faddchar | 补位符 | varchar | 50 |  | √ | ' ' | 补位符 |
| 13 | fvalueatribute | 编码来源 | varchar | 50 |  | √ | ' ' | 编码来源 |
| 14 | fsplitsign | 段间分隔符 | varchar | 50 |  | √ | ' ' | 段间分隔符,枚举: |
| 15 | fcutstyle | 右侧截取 | varchar | 1 |  | √ | '1' | 右侧截取 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fattributetype | 属性类型 | varchar | 50 |  | √ | ' ' | 属性类型,枚举: 1 :常量 2 :创建日期 16 :流水号 4 :文本资料 8 :基础资料 64 :系统资料 |
| 18 | fvalueatributeshow | 编码来源 | varchar | 50 |  |  | ' ' | 编码来源 |
| 19 | fissplitsign | 段间分隔 | bpchar | 1 |  | √ | '1' | 段间分隔 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_drawnoruleentry_fk |  | fid |
| 2 | pk_t_plmdc_drawnoruleentry |  | fentryid |
