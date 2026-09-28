# ID生成器-号段-bos_signer_segment

## ID生成器-号段-多语言表 t_signer_segment_l

- **表名称：** ID生成器-号段-多语言表
- **表名：** t_signer_segment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_signer_segment_l_fname |  | fname |
| 2 | idx_t_signer_segment_l_fid |  | fid,flocaleid |
| 3 | pk_t_signer_segment_l |  | fpkid |

---

## 单据体-子表 t_signer_segmententry

- **表名称：** 单据体-子表
- **表名：** t_signer_segmententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fcurseq | 当前号 | int8 | 64 |  | √ | 0 | 当前号 |
| 3 | fkey | 关键字 | varchar | 512 |  | √ | ' ' | 关键字 |
| 4 | fupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 5 | fdeletetag | 删除标记 | bpchar | 1 |  | √ | '0' | 删除标记 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmaxseq | 最大号 | int8 | 64 |  | √ | 0 | 最大号 |
| 8 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_signer_segmententry |  | fentryid |
| 2 | idx_signer_segmententry_key |  | fkey |

---

## ID生成器-号段-主表 t_signer_segment

- **表名称：** ID生成器-号段-主表
- **表名：** t_signer_segment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsegmentlength | 号段长度 | int8 | 64 |  | √ | 0 | 号段长度 |
| 5 | fmaxseq | 最大号 | int8 | 64 |  | √ | 0 | 最大号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcurseq | 当前号 | int8 | 64 |  | √ | 0 | 当前号 |
| 11 | fkey | 关键字 | varchar | 512 |  | √ | ' ' | 关键字 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fversion | 版本 | int4 | 32 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_signer_segment |  | fid |
| 2 | idx_signer_segment_key |  | fkey |
