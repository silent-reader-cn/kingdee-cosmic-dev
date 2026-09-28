# 专家培训F7-src_experttrainf7

## 专家培训F7-主表 t_src_experttrain

- **表名称：** 专家培训F7-主表
- **表名：** t_src_experttrain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpertid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | faptitudename | faptitudename | varchar | 255 |  | √ | ' ' |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fisselfhelp | fisselfhelp | bpchar | 1 |  | √ | '0' |  |
| 9 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 10 | faptitudenumber | faptitudenumber | varchar | 50 |  | √ | ' ' |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | faptitudetypeid | faptitudetypeid | int8 | 64 |  | √ | 0 |  |
| 13 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 培训编号 | varchar | 30 |  | √ | ' ' | 培训编号 |
| 15 | fgrade | fgrade | varchar | 50 |  | √ | ' ' |  |
| 16 | fitemtypeid | 类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 17 | fbizorg | fbizorg | varchar | 255 |  | √ | ' ' |  |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 20 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 21 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 22 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 23 | fischanged | fischanged | bpchar | 1 |  | √ | '0' |  |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | fbegindate | fbegindate | timestamp | 0 |  |  | null |  |
| 28 | faptitudenote | faptitudenote | varchar | 50 |  | √ | ' ' |  |
| 29 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 30 | fdescription | fdescription | varchar | 1020 |  | √ | ' ' |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fissuedate | fissuedate | timestamp | 0 |  |  | null |  |
| 33 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 34 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 35 | fissueorg | fissueorg | varchar | 255 |  | √ | ' ' |  |
| 36 | fitemname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 37 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_experttrain |  | fid |
| 2 | idx_src_experttrain_fbillno |  | fbillno |
| 3 | idx_src_experttrain_fexpertid |  | fexpertid |
